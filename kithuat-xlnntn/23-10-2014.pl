%nam hoc bai
s(S) --> np(NP,X),vp(NP^S,X).

np(NP,X) --> nnp(NP,X).
np(NP,X) --> nn(NP,X).

vp(VP,X) --> vb(VP,X,_).
vp(VP,X) --> vb(NP^VP,X,Y),np(NP,Y).

nnp(LF,X) --> [W],{lexicon(W,nnp,LF,X)}.
nn(LF,X) --> [W],{lexicon(W,nn,LF,X)}.
vb(LF,X,Y) --> [W],{lexicon(W,vb,LF,X,Y)}.

lexicon(nam,nnp,nam,subj).
lexicon(bai,nn,bai,obj).

lexicon(hoc,vb,X^hoc(X),subj,_).
lexicon(hoc,vb,Y^X^hoc(X,Y),subj,obj).

%nam hoc bai o nha
vp(VP1,X) --> vp1(PP^VP1,X),pp(PP).
pp(IN) --> in(NP^IN,X),np(NP,X).
in(X,Z) --> [Y],{lexicon(Y,in,X,Z)}.
lexicon(o,in,X^o(X),obj1).

vp1(VB,X) --> vb(NP^VB,X,Y),np(NP,Y).

%vb(X) --> [Y],{lexicon(Y,vb,X)}.
lexicon(hoc,vb,X^Y^Z^hoc(Z,X,Y),subj,obj).
lexicon(nha,nn,nha,obj1).
lexicon(toan,nn,toan,obj).






