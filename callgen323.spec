Summary:	H.323 call generator
Summary(pl):	Generator po³±czeñ H.323
Name:		callgen323
Version:	1.2.4
Release:	1
License:	MPL
Group:		Networking/Daemons
Source0:	http://www.openh323.org/bin/%{name}_%{version}.tar.gz
Patch0:		%{name}-mak_files.patch
URL:		http://www.openh323.org/
BuildRequires:	openh323-devel >= 1.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%requires_eq	openh323

%description
What you can do with this call generator:
 - spawning an exact number of calls.
 - receiving an exact number of calls.
 - adjust the delay between each batch of calls.
 - set the number of batches to repeat.
 - The only capability supported is G.711 ULaw 64k and user indication.

%description -l pl
Co mo¿esz robiæ tym generatorem po³±czeñ:
 - utworzyæ dowoln± ilo¶æ po³±czeñ.
 - odebraæ dowoln± ilo¶æ po³±czeñ.
 - ustawiæ opó¼nienie miêdzy dowoln± parti± po³±czeñ.
 - ustawiæ ilo¶æ partii po³±czeñ do powtórzenia.
 - Jedyn± dostêpn± mo¿liwo¶ci± jest G.711 ULaw 64k oraz wskazania u¿ytkownika.

%prep
%setup -qn %{name}
%patch0 -p1

%build
PWLIBDIR=%{_prefix}; export PWLIBDIR
OPENH323DIR=%{_prefix}; export OPENH323DIR

%{__make} optshared OPTCCFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install obj_*/%{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/*
