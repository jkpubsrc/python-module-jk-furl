#!/usr/bin/python3


from jk_testing import Assert

from jk_furl import *







TEST_VECTOR_1 = (
	(	"A1",	"/",		"/ab.cd",				"/ab.cd"			),
	(	"A2",	"/",		"ab.cd",				"/ab.cd"			),
	(	"A3",	"/xy/z/",	"ab.cd",				"/xy/z/ab.cd"		),
	(	"A4",	"/xy/z/",	"../ab.cd",				"/xy/ab.cd"			),
	(	"A5",	"/xy/z/",	".././ab.cd",			"/xy/ab.cd"			),
	(	"A6",	"/xy/z/",	".././../ab.cd",		"/ab.cd"			),
	(	"A7",	"/xy/z/",	".././../../ab.cd",		"/../ab.cd"			),
	(	"A8",	"/xy/z/",	"/a/ab.cd",				"/a/ab.cd"			),
	(	"A9",	"/xy/z/",	"/../ab.cd",			"/../ab.cd"			),
)

for label, mergeURL1, mergeURL2, validationURL in TEST_VECTOR_1:
	print(label)
	Assert.isEqual(
		mergeURLPaths(mergeURL1, mergeURL2),
		validationURL
	)


print()



urlCanonicalizer = URLCanonicalizer("https://www.xyz/startx/")


TEST_VECTOR_2 = (
	(	"B1",	"http://test.abc/def.yz",	"http://test.abc/def.yz",				),
	(	"B2",	"//test.abc/def.yz",		"https://test.abc/def.yz",				),
	(	"B3", 	"http:///def.yz",			"http://www.xyz/def.yz",				),
	(	"B4", 	"/def.yz",					"https://www.xyz/def.yz",				),
	(	"B5", 	"///rtz.hu",				"https://rtz.hu/startx/",				),
	(	"B6", 	"def.yz",					"https://www.xyz/startx/def.yz",		),
)


for label, testURL, validationURL in TEST_VECTOR_2:
	print(label + "a")
Assert.isEqual(urlCanonicalizer(testURL), validationURL)

print()

for label, testURL, validationURL in TEST_VECTOR_2:
	print(label + "b")
Assert.isEqual(urlCanonicalizer(testURL + "#abc"), validationURL + "#abc")








