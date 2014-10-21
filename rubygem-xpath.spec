# Generated from xpath-0.1.4.gem by gem2rpm5 0.6.5 -*- rpm-spec -*-
%define	rbname	xpath

Summary:	Generate XPath expressions from Ruby
Name:		rubygem-%{rbname}

Version:	2.0.0
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://github.com/jnicklas/xpath
Source0:	http://rubygems.org/gems/xpath-2.0.0.gem
Source1:	%{name}.rpmlintrc
BuildRequires:	rubygems 
BuildArch:	noarch

%description
XPath is a Ruby DSL for generating XPath expressions

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f spec/

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/xpath
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/xpath/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/spec
%{ruby_gemdir}/gems/%{rbname}-%{version}/spec/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/spec/fixtures
%{ruby_gemdir}/gems/%{rbname}-%{version}/spec/fixtures/*.html
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
