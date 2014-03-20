# Generated from xpath-0.1.4.gem by gem2rpm5 0.6.5 -*- rpm-spec -*-
%define	rbname	xpath

Summary:	Generate XPath expressions from Ruby
Name:		rubygem-%{rbname}

Version:	0.1.4
Release:	2
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://github.com/jnicklas/xpath
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
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
%{ruby_gemdir}/doc/%{rbname}-%{version}
%{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc



%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.1.4-2
+ Revision: 774161
- mass rebuild of ruby packages against ruby 1.9.1

* Wed Oct 05 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.1.4-1
+ Revision: 703096
- imported package rubygem-xpath


* Wed Oct 05 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.1.4-1
- Initial package generated by gem2rpm5
