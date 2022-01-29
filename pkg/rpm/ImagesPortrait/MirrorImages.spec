Name: ImagesPortrait
Version:    %{_version}
Release:    %{_release}
Summary:    MirrorImages portrait mode images
License:    MIT
BuildArch:  noarch
Requires:   MirrorCommand
URL:        https://gitlab.com/doctorfree/MirrorImages
Vendor:     Doctorwhen's Bodacious Laboratory
Packager:   ronaldrecord@gmail.com

%global __os_install_post %{nil}

%description
Portrait mode images for the MirrorCommand MagicMirror management package

%prep

%build

%install
cp -a %{_sourcedir}/usr %{buildroot}/usr

%post
exec 1>/proc/${PPID}/fd/1
exec 2>/proc/${PPID}/fd/2
export PATH=/usr/local/bin:$PATH

export PATH=/usr/local/bin:$PATH
MM="/usr/local/MirrorCommand"
PICDIR="${MM}/pics-portrait"
[ -d ${PICDIR} ] || mkdir ${PICDIR}
cd ${PICDIR}
DOWNLOAD=
if [ -f ${PICDIR}/imlist.txt ]
then
  while read img
  do
    [ -f ${PICDIR}/${img} ] || {
        DOWNLOAD=1
        break
    }
  done < ${PICDIR}/imlist.txt
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
  if [ -x ${MM}/bin/getimages ]
  then
    echo "Downloading portrait mode image archive ..."
    ${MM}/bin/getimages
  else
    echo "Unable to locate ${MM}/bin/getimages"
    echo "Verify that MirrorCommand is installed and"
    echo "${MM}/bin/getimages is executable, then"
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
    if [ -f ${MM}/pics-portrait/imlist.txt ]
    then
      while read img
      do
        rm -f ${MM}/pics-portrait/${img}
      done < ${MM}/pics-portrait/imlist.txt
      rm -f ${MM}/pics-portrait/imlist.txt
      for subdir in Art Fractals Gif Owls Waterfalls
      do
        for folder in ${MM}/pics-portrait/${subdir}/*
        do
          [ "${folder}" == "${MM}/pics-portrait/${subdir}/*" ] || {
            [ -d ${folder} ] && {
              if [ -L ${folder} ]
              then
                rm -f ${folder}
              else
                rmdir --ignore-fail-on-non-empty ${folder}
              fi
            }
          }
        done
        [ -d ${MM}/pics-portrait/${subdir} ] && {
          if [ -L ${MM}/pics-portrait/${subdir} ]
          then
            rm -f ${MM}/pics-portrait/${subdir}
          else
            rmdir --ignore-fail-on-non-empty ${MM}/pics-portrait/${subdir}
          fi
        }
      done
    else
      for subdir in Art Fractals Gif Owls Waterfalls
      do
        rm -rf ${MM}/pics-portrait/${subdir}
      done
    fi
    # Remove any symbolic links in the pics-portrait directory
    for folder in ${MM}/pics-portrait/*
    do
      [ "${folder}" == "${MM}/pics-portrait/*" ] && continue
      [ -L "${folder}" ] && {
          rm -f "${folder}"
      }
    done
}
echo "MirrorImages pre-installation configuration complete"

%files
/usr

%changelog
