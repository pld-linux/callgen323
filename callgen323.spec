Summary:	H.323 call generator
Summary(pl):	Generator po³±czeñ H.323
Name:		callgen323
Version:	1.2.6
Release:	3
License:	MPL 1.0
Group:		Networking/Daemons
Source0:	http://www.openh323.org/bin/%{name}_%{version}.tar.gz
# Source0-md5:	1428f738e3ad43e5c57aa99e132065dc
Patch0:		%{name}-mak_files.patch
URL:		http://www.openh323.org/
BuildRequires:	openh323-devel >= 1.12.0
BuildRequires:	pwlib-devel >= 1.4.8
%requires_eq	openh323
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%{__make} %{?debug:debug}%{!?debug:opt}shared \
	OPTCCFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"

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
