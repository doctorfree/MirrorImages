Name: CountriesLandscape
Version:    %{_version}
Release:    %{_release}
Summary:    MirrorImages Countries model landscape mode images
License:    MIT
BuildArch:  noarch
Requires:   MirrorCommand >= 3.0.2
URL:        https://gitlab.com/doctorfree/MirrorImages
Vendor:     Doctorwhen's Bodacious Laboratory
Packager:   ronaldrecord@gmail.com

%global __os_install_post %{nil}

%description
Landscape mode Countries images for the MirrorCommand MagicMirror management package

%prep

%build

%install
cp -a %{_sourcedir}/usr %{buildroot}/usr

%post
exec 1>/proc/${PPID}/fd/1
exec 2>/proc/${PPID}/fd/2
export PATH=/usr/local/bin:$PATH

MM="/usr/local/MirrorCommand"
PICDIR="${MM}/pics-landscape"
USER=$(stat -c '%U' ${MM}/config)
GROUP=$(stat -c '%G' ${MM}/config)
[ -d ${PICDIR} ] || mkdir ${PICDIR}
cd ${PICDIR}
DOWNLOAD=
if [ -f ${PICDIR}/countrieslist.txt ]
then
  while read img
  do
    [ -f ${PICDIR}/${img} ] || {
        DOWNLOAD=1
        break
    }
  done < ${PICDIR}/countrieslist.txt
else
  DOWNLOAD=1
fi
[ "${DOWNLOAD}" ] && {
  type -p pip > /dev/null || {
    if type -p dnf > /dev/null
    then
      dnf -q -y install python-pip
    else
      if type -p yum > /dev/null
      then
        yum -q -y install python-pip
      else
        echo "Unable to locate dnf or yum"
        echo "Verify that dnf or yum is installed"
        echo "then retry installation of this package."
      fi
    fi
  }
  pip list | grep -F gdown > /dev/null || {
    pip install gdown
  }
  if [ -x ${MM}/bin/getcountries ]
  then
    echo "Downloading landscape mode Countries image archive ..."
    ${MM}/bin/getcountries -l -i
  else
    echo "Unable to locate ${MM}/bin/getcountries"
    echo "Verify that MirrorCommand is installed and"
    echo "${MM}/bin/getcountries is executable, then"
    echo "retry installation of this package."
  fi
}
chown -R ${USER}:${GROUP} ${MM}
echo "MirrorImages installation Complete"

%preun
exec 1>/proc/${PPID}/fd/1
exec 2>/proc/${PPID}/fd/2
export PATH=/usr/local/bin:$PATH
MM="/usr/local/MirrorCommand"
[ -d ${MM}/pics-landscape ] && {
    if [ -f ${MM}/pics-landscape/countrieslist.txt ]
    then
      while read img
      do
        rm -f ${MM}/pics-landscape/${img}
      done < ${MM}/pics-landscape/countrieslist.txt
      rm -f ${MM}/pics-landscape/countrieslist.txt
      for subdir in ${MM}/pics-landscape/Countries/*
      do
        [ "${subdir}" == "${MM}/pics-landscape/Countries/*" ] && continue
        [ -d ${subdir} ] && {
          if [ -L ${subdir} ]
          then
            rm -f ${subdir}
          else
            rmdir --ignore-fail-on-non-empty ${subdir}
          fi
        }
      done
      [ -d ${MM}/pics-landscape/Countries ] && {
        if [ -L ${MM}/pics-landscape/Countries ]
        then
          rm -f ${MM}/pics-landscape/Countries
        else
          rmdir --ignore-fail-on-non-empty ${MM}/pics-landscape/Countries
        fi
      }
    else
      rm -rf ${MM}/pics-landscape/Countries
    fi
}
echo "MirrorImages pre-installation configuration complete"

%files
/usr
%exclude %dir /usr/local/MirrorCommand
%exclude %dir /usr/local/share/doc
%exclude %dir /usr/local/share
%exclude %dir /usr/local
%exclude %dir /usr

%changelog
