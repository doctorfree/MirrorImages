Name: JavPortrait
Version:    %{_version}
Release:    %{_release}
Summary:    MirrorImages JAV portrait mode images
License:    MIT
BuildArch:  noarch
Requires:   MirrorCommand
URL:        https://gitlab.com/doctorfree/MirrorImages
Vendor:     Doctorwhen's Bodacious Laboratory
Packager:   ronaldrecord@gmail.com

%global __os_install_post %{nil}

%description
Portrait mode JAV images for the MirrorCommand MagicMirror management package

%prep

%build

%install
cp -a %{_sourcedir}/usr %{buildroot}/usr

%post
exec 1>/proc/${PPID}/fd/1
exec 2>/proc/${PPID}/fd/2
export PATH=/usr/local/bin:$PATH

MM="/usr/local/MirrorCommand"
PICDIR="${MM}/pics-portrait"
[ -d ${PICDIR} ] || mkdir ${PICDIR}
cd ${PICDIR}
DOWNLOAD=
if [ -f ${PICDIR}/javlist.txt ]
then
  while read img
  do
    [ -f ${PICDIR}/${img} ] || {
        DOWNLOAD=1
        break
    }
  done < ${PICDIR}/javlist.txt
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
  if [ -x ${MM}/bin/getjav ]
  then
    echo "Downloading portrait mode JAV image archive ..."
    ${MM}/bin/getjav
  else
    echo "Unable to locate ${MM}/bin/getjav"
    echo "Verify that MirrorCommand is installed and"
    echo "${MM}/bin/getjav is executable, then"
    echo "retry installation of this package."
  fi
}
echo "MirrorImages installation Complete"

%preun
exec 1>/proc/${PPID}/fd/1
exec 2>/proc/${PPID}/fd/2
export PATH=/usr/local/bin:$PATH
MM="/usr/local/MirrorCommand"
[ -d ${MM}/pics-portrait ] && {
    if [ -f ${MM}/pics-portrait/javlist.txt ]
    then
      while read img
      do
        rm -f ${MM}/pics-portrait/${img}
      done < ${MM}/pics-portrait/javlist.txt
      rm -f ${MM}/pics-portrait/javlist.txt
      for subdir in ${MM}/pics-portrait/JAV/*
      do
        [ "${subdir}" == "${MM}/pics-portrait/JAV/*" ] && continue
        [ -d ${subdir} ] && {
          if [ -L ${subdir} ]
          then
            rm -f ${subdir}
          else
            rmdir --ignore-fail-on-non-empty ${subdir}
          fi
        }
      done
      [ -d ${MM}/pics-portrait/JAV ] && {
        if [ -L ${MM}/pics-portrait/JAV ]
        then
          rm -f ${MM}/pics-portrait/JAV
        else
          rmdir --ignore-fail-on-non-empty ${MM}/pics-portrait/JAV
        fi
      }
    else
      rm -rf ${MM}/pics-portrait/JAV
    fi
}
echo "MirrorImages pre-installation configuration complete"

%files
/usr

%changelog
