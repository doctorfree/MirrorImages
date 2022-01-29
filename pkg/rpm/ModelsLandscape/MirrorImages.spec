Name: ModelsLandscape
Version:    %{_version}
Release:    %{_release}
Summary:    MirrorImages Models landscape mode images
License:    MIT
BuildArch:  noarch
Requires:   MirrorCommand
URL:        https://gitlab.com/doctorfree/MirrorImages
Vendor:     Doctorwhen's Bodacious Laboratory
Packager:   ronaldrecord@gmail.com

%global __os_install_post %{nil}

%description
Landscape mode Models images for the MirrorCommand MagicMirror management package

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
[ -d ${PICDIR} ] || mkdir ${PICDIR}
cd ${PICDIR}
DOWNLOAD=
if [ -f ${PICDIR}/modelslist.txt ]
then
  while read img
  do
    [ -f ${PICDIR}/${img} ] || {
        DOWNLOAD=1
        break
    }
  done < ${PICDIR}/modelslist.txt
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
  if [ -x ${MM}/bin/getmodels ]
  then
    echo "Downloading landscape mode Models image archive ..."
    ${MM}/bin/getmodels -l
  else
    echo "Unable to locate ${MM}/bin/getmodels"
    echo "Verify that MirrorCommand is installed and"
    echo "${MM}/bin/getmodels is executable, then"
    echo "retry installation of this package."
  fi
}
echo "MirrorImages installation Complete"

%preun
exec 1>/proc/${PPID}/fd/1
exec 2>/proc/${PPID}/fd/2
export PATH=/usr/local/bin:$PATH
MM="/usr/local/MirrorCommand"
[ -d ${MM}/pics-landscape ] && {
    if [ -f ${MM}/pics-landscape/modelslist.txt ]
    then
      while read img
      do
        rm -f ${MM}/pics-landscape/${img}
      done < ${MM}/pics-landscape/modelslist.txt
      rm -f ${MM}/pics-landscape/modelslist.txt
      for subdir in ${MM}/pics-landscape/Models/*
      do
        [ "${subdir}" == "${MM}/pics-landscape/Models/*" ] && continue
        [ -d ${subdir} ] && {
          if [ -L ${subdir} ]
          then
            rm -f ${subdir}
          else
            rmdir --ignore-fail-on-non-empty ${subdir}
          fi
        }
      done
      [ -d ${MM}/pics-landscape/Models ] && {
        if [ -L ${MM}/pics-landscape/Models ]
        then
          rm -f ${MM}/pics-landscape/Models
        else
          rmdir --ignore-fail-on-non-empty ${MM}/pics-landscape/Models
        fi
      }
    else
      rm -rf ${MM}/pics-landscape/Models
    fi
}
echo "MirrorImages pre-installation configuration complete"

%files
/usr

%changelog
