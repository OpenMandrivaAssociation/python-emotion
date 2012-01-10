#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/BINDINGS/python/python-emotion python-emotion; \
#cd python-emotion; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#v_maj=$(cat configure.ac | grep 'm4_define(\[v_maj\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_min=$(cat configure.ac | grep 'm4_define(\[v_min\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_mic=$(cat configure.ac | grep 'm4_define(\[v_mic\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#PKG_VERSION=$v_maj.$v_min.$v_mic.$SVNREV; \
#cd ..; \
#tar -Jcf python-emotion-$PKG_VERSION.tar.xz python-emotion/ --exclude .svn --exclude .*ignore

%define svnrev  65723

Summary:	Emotion bindings for Python 
Name:		python-emotion
Version:	0.7.3
Release:	0.%{svnrev}.1
Group:		Graphical desktop/Enlightenment
License:	GPLv2
URL:		http://www.enlightenment.org/
Source0:	%{name}-%{version}.%{svnrev}.tar.xz
# It checks for emotion version 0.2.0 svn release >= 52190 but since we remove the .svn stuff from the tarballs
# the svn release is not properly set. Ignore it
Patch1:		python-emotion-do_not_check_for_emotion_svn_rel.patch

BuildRequires:	pkgconfig(eina)
BuildRequires:	pkgconfig(emotion)
BuildRequires:	pkgconfig(python-evas)
BuildRequires:	python-cython
%py_requires -d

%description
Python support files for Emotion

%package devel
Summary:    Development files for %{name}
Group:      Development/Python

%description devel
Development files for the Python wrapper for the Emotion libraries.

%prep
%setup -qn %{name}
%patch1 -p1

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%doc README
%{py_platsitedir}/emotion/*

%files devel
%{_datadir}/%{name}/*
%{_libdir}/pkgconfig/*.pc

