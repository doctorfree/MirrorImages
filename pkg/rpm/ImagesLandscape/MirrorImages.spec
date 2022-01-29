Name: ImagesLandscape
Version:    %{_version}
Release:    %{_release}
Summary:    MirrorImages landscape mode images
License:    MIT
BuildArch:  noarch
Requires:   MirrorCommand >= 3.0.2
URL:        https://gitlab.com/doctorfree/MirrorImages
Vendor:     Doctorwhen's Bodacious Laboratory
Packager:   ronaldrecord@gmail.com

%global __os_install_post %{nil}

%description
Landscape mode images for the MirrorCommand MagicMirror management package

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
PICDIR="${MM}/pics-landscape"
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
    echo "Downloading landscape mode image archive ..."
    ${MM}/bin/getimages -l -i
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
[ -d ${MM}/pics-landscape ] && {
    if [ -f ${MM}/pics-landscape/imlist.txt ]
    then
      while read img
      do
        rm -f ${MM}/pics-landscape/${img}
      done < ${MM}/pics-landscape/imlist.txt
      rm -f ${MM}/pics-landscape/imlist.txt
      for subdir in Art Fractals Gif Owls Waterfalls
      do
        for folder in ${MM}/pics-landscape/${subdir}/*
        do
          [ "${folder}" == "${MM}/pics-landscape/${subdir}/*" ] || {
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
        [ -d ${MM}/pics-landscape/${subdir} ] && {
          if [ -L ${MM}/pics-landscape/${subdir} ]
          then
            rm -f ${MM}/pics-landscape/${subdir}
          else
            rmdir --ignore-fail-on-non-empty ${MM}/pics-landscape/${subdir}
          fi
        }
      done
    else
      for subdir in Art Fractals Gif Owls Waterfalls
      do
        rm -rf ${MM}/pics-landscape/${subdir}
      done
    fi
    # Remove any symbolic links in the pics-landscape directory
    for folder in ${MM}/pics-landscape/*
    do
      [ "${folder}" == "${MM}/pics-landscape/*" ] && continue
      [ -L "${folder}" ] && {
          rm -f "${folder}"
      }
    done
}
echo "MirrorImages pre-removal configuration complete"

%files
/usr

%changelog
