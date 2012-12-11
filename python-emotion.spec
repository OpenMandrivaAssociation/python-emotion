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

Summary:	Emotion bindings for Python 
Name:		python-emotion
Version:	1.7.0
Release:	1
Group:		Graphical desktop/Enlightenment
License:	GPLv2
URL:		http://www.enlightenment.org/
Source0:	http://download.enlightenment.org/releases/BINDINGS/python/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig(eina)
BuildRequires:	pkgconfig(emotion)
BuildRequires:	pkgconfig(python-evas)
BuildRequires:	python-cython
%py_requires -d

%description
Python support files for Emotion.

%package devel
Summary:	Development files for %{name}
Group:		Development/Python

%description devel
Development files for the Python wrapper for the Emotion libraries.

%prep
%setup -q
%patch1 -p1

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc README
%{py_platsitedir}/emotion/*

%files devel
%{_datadir}/%{name}/*
%{_libdir}/pkgconfig/*.pc



%changelog
* Tue Jan 10 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.7.3-0.65723.1
+ Revision: 759628
- imported package python-emotion


* Tue Jan 10 2012 Matthew Dawkins <mdawkins@unity-linux.org> 0.7.3-0.65723.1-unity2011
- new version 0.7.3

* Wed Aug 24 2011 Gianvacca <gianvacca@unity-linux.org> 0.7.3.56327-0.20110824.1-unity2011
- new snapshot
- added patch 1

* Sat Mar 05 2011 OnlyHuman <halo.3.0sdt@googlemail.com> 0.0.1-0.20110305.beta3.1-unity2011
- new version 1.0.0 beta3 svn 20110305

* Fri Jan 14 2011 OnlyHuman <halo.3.0sdt@googlemail.com> 0.0.1-0.20110114.beta3.1-unity2011
- new version 1.0.0 beta3 svn 20110114

* Mon Dec 13 2010 OnlyHuman <halo.3.0sdt@googlemail.com> 0.0.1-0.20101203.beta3.1-unity2010
- new version 1.0.0 beta3 svn 20101203

* Mon Oct 11 2010 mdawkins <mattydaw@gmail.com> 0.0.1-0.20101006.1-unity2010
- new snapshot 20101006

* Thu Aug 26 2010 mdawkins <mattydaw@gmail.com> 0.0.1-0.20100825.1-unity2010
- new version 0.0.1
