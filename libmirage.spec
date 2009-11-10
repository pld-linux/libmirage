# TODO: package docs
Summary:	CD-ROM image access library
Summary(pl.UTF-8):	Biblioteka do obsługi obrazów CD-ROM
Name:		libmirage
Version:	1.2.0
Release:	0.5
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/cdemu/%{name}-%{version}.tar.bz2
# Source0-md5:	816e61eb72c2851bcf9a074f6249a336
URL:		http://www.cdemu.org/
BuildRequires:	glib2-devel >= 1:2.6
BuildRequires:	gtk-doc-automake >= 1.4
BuildRequires:	libsndfile-devel >= 1.0.0
BuildRequires:	libstdc++-devel >= 5:3.2
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CD-ROM image access library.

%description -l pl.UTF-8
Biblioteka do obsługi obrazów CD-ROM.

%package devel
Summary:	libmirage development package
Summary(pl.UTF-8):	libmirage - część dla programistów
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel >= 5:3.2

%description devel
Header files for libmirage.

%description devel -l pl.UTF-8
Pliki nagłówkowe do biblioteki libmirage.

%package static
Summary:	libmirage static library
Summary(pl.UTF-8):	Statyczna biblioteka libmirage
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libmirage.

%description static -l pl.UTF-8
Statyczna wersja biblioteki libmirage.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
#%doc AUTHORS ChangeLog INSTALL README
%attr(755,root,root) %ghost %{_libdir}/libmirage.so.?
%attr(755,root,root) %{_libdir}/libmirage.so.*.*.*
%dir %{_libdir}/libmirage-1.2
%attr(755,root,root) %{_libdir}/libmirage-*/*.so

%{_datadir}/mime/packages/libmirage*.xml

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmirage.so
%{_libdir}/*.la
%{_libdir}/libmirage-*/*.la
%{_includedir}/libmirage
%{_pkgconfigdir}/libmirage.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_libdir}/libmirage-*/*.a
