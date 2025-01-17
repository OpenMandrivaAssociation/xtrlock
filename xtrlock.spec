

Summary:	Minimal X display lock program
Name:		xtrlock
Version:	2.15
Release:	1
Group:		Graphical desktop/Other
URL:		https://packages.debian.org/sid/xtrlock
BuildRequires:	pkgconfig(x11)
BuildRequires:	imake
License:	GPLv2+
Source0:	http://ftp.de.debian.org/debian/pool/main/x/%{name}/%{name}_2.15.tar.xz

%description
xtrlock is a very minimal X display lock program, which uses nothing
except the Xlib library. It doesn't obscure the screen, it is
completely idle while the display is locked and you don't type at it,
and it doesn't do funny things to the X access control lists. 

%prep
%setup -q

%build
xmkmf
%make CFLAGS="%{optflags}" xtrlock

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 755 xtrlock %{buildroot}%{_bindir}/%{name}
install -m 644 xtrlock.man %{buildroot}%{_mandir}/man1/%{name}.1x

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=Xtrlock
Comment=X terminal lock
Exec=%{_bindir}/%{name} 
Icon=gnome-lockscreen
Terminal=false
Type=Application
StartupNotify=true
Categories=System;
EOF

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc debian/README.Debian
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/mandriva-%{name}.desktop


%changelog
* Mon Sep 21 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.0-2mdv2010.0
+ Revision: 446272
- rebuild

* Wed Dec 24 2008 Adam Williamson <awilliamson@mandriva.org> 2.0-1mdv2009.1
+ Revision: 318409
- buildrequires imake
- import xtrlock


