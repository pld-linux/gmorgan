Summary:	Modern organ and a rhythm station
Summary(pl.UTF-8):	Nowoczesne organy oraz stacja rytmiczna
Name:		gmorgan
Version:	0.25
Release:	1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/gmorgan/%{name}-%{version}.tar.gz
# Source0-md5:	c74842cd5ecde1d83799d362114b7f34
URL:		http://gmorgan.sourceforge.net/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fltk-devel
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gmorgan is a rhythm station, a modern organ with full editable
accompaniment for play in real time emulating the capabilities of
commercial rhythm stations "Korg","Roland","Solton", also has a small
pattern based sequencer like "Band in a Box". Uses the capabilities of
ALSA sequencer to produce MIDI accompaniment.

%description -l pl.UTF-8
Gmorgan to stacja rytmiczna, nowoczesne organy z pełną edycją
akompaniamentu do otwarzania muzyki w czasie rzeczywistym, emulująca
jednocześnie możliwości komercyjnych produktów firm takich jak
"Korg", "Roland", "Solton", wyposażona także w mały sekwenser
podobny do "Band in a Box". Gmorgan wykorzystuje możliwości
sekwensera ALSA do tworzenia akompaniamentów MIDI.

%prep
%setup -q

%build
%{__gettextize}
%{__aclocal} -I m4
%{__automake}
%{__autoconf}

%configure \
	--disable-dependency-tracking

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gmorgan
%dir %{_datadir}/gmorgan
%{_datadir}/gmorgan/*
