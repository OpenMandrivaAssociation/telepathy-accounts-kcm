%define major      4
%define libname    %mklibname %{name} %{major}
%define develname  %mklibname -d %{name}

%define git git20111005
%define rel 1

Summary:	KControl Module which handles Telepathy Accounts
Name:		telepathy-accounts-kcm
Version:	0.1
Release:	%mkrel -c %{git} %{rel}
Url:		https://projects.kde.org/projects/playground/network/telepathy/telepathy-accounts-kcm
Source0:	telepathy-accounts-kcm-%{version}-%{git}.tar.xz
License:	GPLv2+
Group:		Graphical desktop/KDE
BuildRequires:	kdelibs4-devel
BuildRequires:	telepathy-qt4-devel >= 0.1.8
Obsoletes:      telepathy-kde-accounts-kcm-plugins

%description
This is a KControl Module which handles adding/editing/removing Telepathy
Accounts. It interacts with any Telepathy Spec compliant AccountManager,
such as telepathy-accountmanager-kwallet to manipulate the accounts. It is
modular in design, with each ConnectionManager-Protocol combination having a
plugin that provides customised forms for adding or editing their accounts,
and also with a generic plugin which can be used as a fallback for
ConnectionManager-Protocol combinations where no plugin exists.

%files
%{_kde_libdir}/kde4/kcm_telepathy_accounts.so
%{_kde_libdir}/kde4/kcmtelepathyaccounts_plugin_butterfly.so
%{_kde_libdir}/kde4/kcmtelepathyaccounts_plugin_gabble.so
%{_kde_libdir}/kde4/kcmtelepathyaccounts_plugin_haze.so
%{_kde_libdir}/kde4/kcmtelepathyaccounts_plugin_idle.so
%{_kde_libdir}/kde4/kcmtelepathyaccounts_plugin_rakia.so
%{_kde_libdir}/kde4/kcmtelepathyaccounts_plugin_salut.so
%{_kde_libdir}/kde4/kcmtelepathyaccounts_plugin_sunshine.so
%{_kde_datadir}/telepathy/profiles/
%{_kde_services}/*.desktop
%{_kde_servicetypes}/*.desktop


#--------------------------------------------------------------------

%package -n %{libname}
Summary:	Library package for %{name}
Group:		Graphical desktop/KDE

%description -n %{libname}
Library package for %{name}.

%files -n %{libname}
%{_kde_libdir}/libkcmtelepathyaccounts.so.%{major}*

#--------------------------------------------------------------------

%package -n %{develname}
Summary:	Development headers for %{name}
Group:		Graphical desktop/KDE
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
This package contains the development headers required to compile software
against %{name}.

%files -n %{develname}
%{_kde_libdir}/libkcmtelepathyaccounts.so

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}

%makeinstall_std -C build

%find_lang %{name}



