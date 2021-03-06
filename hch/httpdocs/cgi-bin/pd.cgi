#!/usr/bin/perl

################################################################
#                                                              #
#                        PerlDiver v1.1                        #
#          Copyright ©1999 - Tintagel Consulting, LLC          #
#                    dba Script Solutions                      #
#               http://www.scriptsolutions.com/                #
#                     All rights reserved                      #
#                                                              #
################################################################
#                                                              #
# PURPOSE OF PROGRAM:                                          #
#                                                              #
# PerlDiver v1.1 gives you the location of your sendmail       #
# program, your path to perl, your environment variables and   #
# most (not all) of the Perl modules that are installed on     #
# your web server.                                             #
#                                                              #
#                                                              #
# INSTRUCTIONS:                                                #
#                                                              #
# Complete instructions and the newest version are located at: #
# http://www.scriptsolutions.com/programs/free/perldiver/      #
#                                                              #
#                                                              #
# LICENSE AGREEMENT:                                           #
#                                                              #
# By downloading and installing PerlDiver v1.1, you have       #
# agreed to indemnify, defend, and hold harmless Tintagel      #
# Consulting, LLC dba Script Solutions from any and all        #
# liability, penalties, losses, damages, costs, expenses,      #
# attorneys' fees, causes of action or claims caused by or     #
# resulting indirectly from your use of this script which      #
# damages either you, or any other party or parties without    #
# limitation or exception. This indemnification and hold       #
# harmless agreement extends to all issues associated with     #
# this script.                                                 #
#                                                              #
################################################################


################################################################
#                DO NOT CHANGE ANYTHING BELOW                  #


print "Content-type: text/html\n\n";

$sendmail       =`whereis sendmail`;
$plocation      =`whereis perl`;

@perlloc = split(" ",$plocation);
@mailloc = split(" ",$sendmail);

$font = '<FONT FACE="Verdana, sans serif" SIZE=2>';
&vars;

print qq~

<HTML>
<HEAD><TITLE></TITLE></HEAD>
<body bgcolor="#FFFFFF" ALINK="#FDB900" LINK="#BF0425" VLINK="#1200FD" TOPMARGIN=0 LEFTMARGIN=0 RIGHTMARGIN=0>
<P ALIGN=CENTER><FONT FACE="Courier New,mono" SIZE=3 COLOR="#BF0425"><B>

<DIV ALIGN=CENTER>

<TABLE WIDTH=100% BGCOLOR=#FDB900 CELLPADDING=2 CELLSPACING=0 BORDER=0><TR><TH>$font<FONT SIZE=4>
Server Program Paths</FONT></TD></TR></TABLE><P>

<TABLE BORDER=0 CELLPADDING=3 WIDTH=95%>
        <TR><TD BGCOLOR="$bgcolor" WIDTH=35%>${font}<B>Perl Executable:</B></TD>
                <TD WIDTH=65%>${font}$^X</TD></TR>

        <TR><TD BGCOLOR="$bgcolor">${font}<B>Perl Version:</B></TD>
                <TD>${font}$]</TD></TR>

        <TR><TD BGCOLOR="$bgcolor">${font}<B>PERL compile version OS:</B></TD>
                <TD>${font}$^O</TD></TR>

        <TR><TD BGCOLOR="$bgcolor">${font}<B>GID</B>: <FONT SIZE=1>(If not blank, you are on a machine that supports membership in 
                multiple groups simultaneously)</FONT></TD>
                <TD>${font}$<</TD></TR>

        <TR><TD VALIGN=TOP BGCOLOR="$bgcolor">${font}<B>Location of Perl:</B></TD>
                <TD>${font}~;

foreach $loc(@perlloc){
        print "$loc<BR>\n";
}
                print qq~</TD></TR>

        <TR><TD VALIGN=TOP BGCOLOR="$bgcolor">${font}<B>Location of Sendmail:</B></TD>
                <TD>${font}~;

foreach $ml(@mailloc){
        print "$ml<BR>\n";
}
                print qq~</TD></TR>

        <TR><TD VALIGN=TOP BGCOLOR="$bgcolor">${font} <B>Directory locations searched for perl executables</B></TD><TD>$font~;

foreach $item(@INC){
        print "$item <BR>\n";
}

        print qq~</TD></TR></TABLE>

<P><TABLE WIDTH=100% BGCOLOR=#FDB900 CELLPADDING=2 CELLSPACING=0 BORDER=0><TR><TH>$font<FONT SIZE=4>
Environment Variables</FONT></TD></TR></TABLE><P>

<TABLE BORDER=0 CELLPADDING=3 WIDTH=95%>

~;
foreach $fieldname(keys %ENV){
        print qq~       <TR><TD BGCOLOR="$bgcolor" WIDTH=35%><B>${font}$fieldname</B></TD>
                <TD WIDTH=65%>${font}$ENV{$fieldname}</TD></TR>~;
}


        print qq~</TABLE>
<P><TABLE WIDTH=100% BGCOLOR=#FDB900 CELLPADDING=2 CELLSPACING=0 BORDER=0><TR><TH>$font<FONT SIZE=4>
Installed Modules</FONT></TD></TR></TABLE><P>

<TABLE BORDER=0 CELLPADDING=3 WIDTH=100%>

~;
find(\&wanted,@INC);

$modcount = 0;

foreach $line(@foundmods){
                $match = lc($line);
                if ($found{$line}[0] >0)        {$found{$line} = [$found{$line}[0]+1,$match]}
                else                            {$found{$line} = ["1",$match];$modcount++}
}

@foundmods = sort count keys(%found);

sub count {return $found{$a}[1] cmp $found{$b}[1]}

$third = $modcount/3;

$count=0;print "<TR><TD WIDTH=33% VALIGN=TOP><TABLE BORDER=0 CELLPADDING=1>";

foreach $mod(@foundmods){
        chomp $mod;
        $count++;
        if ($count <= $third){
                        print qq~<TR><TD>${font}$mod</TD></TR>~;
        }
        else {push (@mod1,$mod)}
}
print "</TABLE></TD><TD WIDTH=33% VALIGN=TOP><TABLE BORDER=0 CELLPADDING=1>";
$count = 0;
foreach $mod1(@mod1){
        chomp $mod1;
        $count++;
        if ($count <= $third){
                        print qq~<TR><TD>${font}$mod1</TD></TR>~;
        }
        else {push (@mod2,$mod1)}
}

print "</TABLE></TD><TD WIDTH=33% VALIGN=TOP><TABLE BORDER=0 CELLPADDING=1>";
$count = 0;
foreach $mod2(@mod2){
        chomp $mod2;
        $count++;
        if ($count <= $third){
                        print qq~<TR><TD>${font}$mod2</TD></TR>~;
        }
}
print qq~</TABLE></TD></TR></TABLE>
<P>
<FONT SIZE=1>$font &copy; 1999, ScriptSolutions, Modified with Permission.<P></BODY></HTML>~;
exit;
sub vars {
$dev="ScriptSolutions™";use File::Find;$bgcolor = "GHOSTWHITE";$program="perl diver";$version="1.1";
}

sub wanted {
        $count = 0;
        if ($File::Find::name =~ /\.pm$/){
                open(MODFILE,$File::Find::name) || return;
                while(<MODFILE>){
                        if (/^ *package +(\S+);/){
                                push (@foundmods, $1);
                                last;
                        }
                } 
        }
}

