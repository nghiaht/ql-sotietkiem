s(VP) --> np(NP), vp(VP), {arg(1,VP,NP)}.

np(X) --> nnp(X).
nnp(nam) --> [nam].

vp(VB) --> vb(VB), np1(NP), {arg(2,VB, NP) }.

vb(mua(_,_)) --> [mua].

np1(PP) --> np2(NP, X), pp(PP, Y), {arg(1,PP,NP), arg(2,PP,Y), arg(1,NP,X)}.


pp(IN,NN) --> in(IN), nn(NN), {arg(2,IN,NN)}.


np2(UN, NN) --> un(UN), nn(NN), {arg(1,UN,NN)}.

nn(thanh_pho) --> [thanh_pho].
in(o(_,_)) --> [o].
un(can(_)) --> [can].
nn(nha) --> [nha].
