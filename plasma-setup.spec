%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Initial setup wizard for Plasma
Name:		plasma-setup
Version:	6.7.5
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
URL:		https://invent.kde.org/plasma/plasma-setup
Source0:	http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz

BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(KF6Auth)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Package)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Screen)
BuildRequires:	cmake(LibKWorkspace)

BuildSystem:	cmake
BuildOption:	-DBUILD_TESTING:BOOL=OFF
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

Requires:	dbus-common
Requires:	polkit

%description
Out-of-the-box first-boot wizard for systems using KDE Plasma.
Guides the user through creating the first account and configuring
language, keyboard, time zone and network.

%files -f %{name}.lang
%{_libexecdir}/plasma-setup
%{_libexecdir}/plasma-setup-bootutil
%{_libdir}/libexec/kf6/kauth/plasma-setup*
%{_qtdir}/qml/org/kde/plasmasetup
%{_qtdir}/plugins/kf6/packagestructure/plasmasetup.so
%{_datadir}/plasma/packages/org.kde.plasmasetup*
%{_datadir}/plasma-setup
%{_datadir}/dbus-1/system-services/org.kde.plasmasetup*
%{_datadir}/dbus-1/system.d/org.kde.plasmasetup*
%{_datadir}/polkit-1/actions/org.kde.plasmasetup*
%{_datadir}/polkit-1/rules.d/plasma-setup*
%{_datadir}/qlogging-categories6/plasmasetup.categories
%config(noreplace) %{_sysconfdir}/xdg/plasmasetuprc
%{_unitdir}/plasma-setup.service
%{_sysusersdir}/plasma-setup.conf
%{_tmpfilesdir}/plasma-setup.conf
