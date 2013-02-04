paulla.doctemplates
===================

set of hosts templates to build hosting sphinx documentation

::
 
    $ bin/paster create --list-templates
    Available templates:
      debian:         A Debian doc template.
      freebsd:        A FreeBSD doc template.
      freebsd-jail:   A FreeBSD  Jail doc template.
      netbsd:         A NetBSD doc template.
      openbsd:        A OpenBSD doc template.
      ubuntu:         An Ubuntu doc template.

install with buildout.cfg
::
     
    [buildout]
    extensions =
        mr.developer

    auto-checkout = 
        paulla.doctemplates

    parts = doc

    develop=

    eggs =
        sphinx
        pastescript
        IPy
        paulla.doctemplates

    [doc]
    recipe=zc.recipe.egg
    eggs =
         ${buildout:eggs}

    [sources]
    paulla.doctemplates = git git@github.com:paulla/paulla.doctemplates.git


::
 
 wget http://svn.zope.org/*checkout*/zc.buildout/trunk/bootstrap/bootstrap.py
 python bootstrap.py -d
 bin/buildout -Nv
 
Start a documentation project

::
 
 bin/sphinx-quickstart
 

edit Makefile line 6 
::
  
 SPHINXBUILD   = bin/sphinx-build


create a specific directory

::
 
 mkdir source/machines
  
a sample non-interactive build from a csv hosts-file

::
 
 cp src/paulla.doctemplates/src/paulla/doctemplates/etc/build_machines.py .
 cp src/paulla.doctemplates/src/paulla/doctemplates/etc/hosts.csv .

  ./build_machines.py
  sh build_doc.sh && make html && browser build/html/genindex.html

You'll like your new doc index, checkout your's conf file in respective directories && enjoy
