Title: white_spaces_can_be_dangerous 
Date: Sat, 19 Dec 2015 23:20:24 -0500
Modified: Sat, 19 Dec 2015 23:20:24 -0500
Category: devops
Tags: Linux
Slug: white_spaces_can_be_dangerous
Authors: Kevin Faulkner
Summary: brief look at go and spacing

====== White spaces can be dangerous  ======
When I was some go I noticed that it refused to compile due to a white space:

''
./go-test-router.go:17: invalid identifier character U+2502
./go-test-router.go:17: syntax error: unexpected name, expecting }
''

I have noticed this first with Microsoft Windows formatting of white spaces and new lines. This is also true Word quotes. This was due to the fact that we had to put documentation on sharepoint. Something I still don't agree with to this day.
