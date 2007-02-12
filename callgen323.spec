Summary:	H.323 call generator
Summary(pl.UTF-8):	Generator połączeń H.323
Name:		callgen323
Version:	1.2.6
Release:	11
License:	MPL 1.0
Group:		Networking/Daemons
Source0:	http://www.openh323.org/bin/%{name}_%{version}.tar.gz
# Source0-md5:	1428f738e3ad43e5c57aa99e132065dc
Patch0:		%{name}-mak_files.patch
Patch1:		%{name}-update.patch
URL:		http://www.openh323.org/
BuildRequires:	openh323-devel >= 1.18.0
BuildRequires:	pwlib-devel >= 1.6.5-3
BuildRequires:	speex-devel
%requires_eq	openh323
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
What you can do with this call generator:
- spawning an exact number of calls.
- receiving an exact number of calls.
- adjust the delay between each batch of calls.
- set the number of batches to repeat.
- The only capability supported is G.711 ULaw 64k and user
  indication.

%description -l pl.UTF-8
Co możesz robić tym generatorem połączeń:
- utworzyć dowolną liczbę połączeń.
- odebrać dowolną liczbę połączeń.
- ustawić opóźnienie między dowolną partią połączeń.
- ustawić liczbę partii połączeń do powtórzenia.
- Jedyną dostępną możliwością jest G.711 ULaw 64k oraz wskazania
  użytkownika.

%prep
%setup -qn %{name}
%patch0 -p1
%patch1 -p1

%build
%{__make} %{?debug:debug}%{!?debug:opt}shared \
	CXX="%{__cxx}" \
	OPTCCFLAGS="%{rpmcflags} -fno-exceptions"

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
