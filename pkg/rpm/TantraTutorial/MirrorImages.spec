Name: TantraTutorial
Version:    %{_version}
Release:    %{_release}
Summary:    MirrorImages TantraTutorial videos
License:    MIT
BuildArch:  noarch
Requires:   MirrorCommand
URL:        https://gitlab.com/doctorfree/MirrorImages
Vendor:     Doctorwhen's Bodacious Laboratory
Packager:   ronaldrecord@gmail.com

%global __os_install_post %{nil}

%description
TantraTutorial videos for the MirrorCommand MagicMirror management package

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
[ -d ${MM}/movies ] || mkdir ${MM}/movies
cd ${MM}/movies
DOWNLOAD=
if [ -f ${MM}/movies/tantralist.txt ]
then
  while read img
  do
    [ -f ${MM}/movies/${img} ] || {
        DOWNLOAD=1
        break
    }
  done < ${MM}/movies/tantralist.txt
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
  if [ -x ${MM}/bin/gettantra ]
  then
    echo "Downloading tantra tutorial archive ..."
    ${MM}/bin/gettantra
  else
    echo "Unable to locate ${MM}/bin/gettantra"
    echo "Verify that MirrorCommand is installed and"
    echo "${MM}/bin/gettantra is executable, then"
    echo "retry installation of this package."
  fi
}
echo "MirrorImages installation Complete"

%preun
exec 1>/proc/${PPID}/fd/1
exec 2>/proc/${PPID}/fd/2
export PATH=/usr/local/bin:$PATH

MM="/usr/local/MirrorCommand"
[ -d ${MM}/movies ] && {
    if [ -f ${MM}/movies/tantralist.txt ]
    then
      while read img
      do
        rm -f ${MM}/movies/${img}
      done < ${MM}/movies/tantralist.txt
      rm -f ${MM}/movies/tantralist.txt
      for subdir in Tantra
      do
        for folder in ${MM}/movies/${subdir}/*
        do
          [ "${folder}" == "${MM}/movies/${subdir}/*" ] || {
            [ -d "${folder}" ] && rmdir --ignore-fail-on-non-empty "${folder}"
          }
        done
        [ -d ${MM}/movies/${subdir} ] && {
            rmdir --ignore-fail-on-non-empty ${MM}/movies/${subdir}
        }
      done
    else
      for subdir in Tantra
      do
        rm -rf ${MM}/movies/${subdir}
      done
    fi
    # Remove any symbolic links in the movies directory
    for folder in ${MM}/movies/*
    do
      [ "${folder}" == "${MM}/movies/*" ] && continue
      [ -L "${folder}" ] && {
          rm -f "${folder}"
      }
    done
}
echo "MirrorImages pre-installation configuration complete"

%files
/usr

%changelog
