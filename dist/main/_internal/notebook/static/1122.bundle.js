"use strict";(self.webpackChunk_JUPYTERLAB_CORE_OUTPUT=self.webpackChunk_JUPYTERLAB_CORE_OUTPUT||[]).push([[1122],{21122:(e,t,n)=>{function r(e){for(var t={},n=e.split(" "),r=0;r<n.length;++r)t[n[r]]=!0;return t}n.r(t),n.d(t,{ttcn:()=>U});const i={name:"ttcn",keywords:r("activate address alive all alt altstep and and4b any break case component const continue control deactivate display do else encode enumerated except exception execute extends extension external for from function goto group if import in infinity inout interleave label language length log match message mixed mod modifies module modulepar mtc noblock not not4b nowait of on optional or or4b out override param pattern port procedure record recursive rem repeat return runs select self sender set signature system template testcase to type union value valueof var variant while with xor xor4b"),builtin:r("bit2hex bit2int bit2oct bit2str char2int char2oct encvalue decomp decvalue float2int float2str hex2bit hex2int hex2oct hex2str int2bit int2char int2float int2hex int2oct int2str int2unichar isbound ischosen ispresent isvalue lengthof log2str oct2bit oct2char oct2hex oct2int oct2str regexp replace rnd sizeof str2bit str2float str2hex str2int str2oct substr unichar2int unichar2char enum2int"),types:r("anytype bitstring boolean char charstring default float hexstring integer objid octetstring universal verdicttype timer"),timerOps:r("read running start stop timeout"),portOps:r("call catch check clear getcall getreply halt raise receive reply send trigger"),configOps:r("create connect disconnect done kill killed map unmap"),verdictOps:r("getverdict setverdict"),sutOps:r("action"),functionOps:r("apply derefers refers"),verdictConsts:r("error fail inconc none pass"),booleanConsts:r("true false"),otherConsts:r("null NULL omit"),visibilityModifiers:r("private public friend"),templateMatch:r("complement ifpresent subset superset permutation"),multiLineStrings:!0};var o=[];function a(e){if(e)for(var t in e)e.hasOwnProperty(t)&&o.push(t)}a(i.keywords),a(i.builtin),a(i.timerOps),a(i.portOps);var s,l=i.keywords||{},c=i.builtin||{},u=i.timerOps||{},p=i.portOps||{},m=i.configOps||{},f=i.verdictOps||{},d=i.sutOps||{},b=i.functionOps||{},h=i.verdictConsts||{},y=i.booleanConsts||{},v=i.otherConsts||{},g=i.types||{},x=i.visibilityModifiers||{},k=i.templateMatch||{},O=i.multiLineStrings,E=!1!==i.indentStatements,w=/[+\-*&@=<>!\/]/;function I(e,t){var n,r=e.next();if('"'==r||"'"==r)return t.tokenize=(n=r,function(e,t){for(var r,i=!1,o=!1;null!=(r=e.next());){if(r==n&&!i){var a=e.peek();a&&("b"!=(a=a.toLowerCase())&&"h"!=a&&"o"!=a||e.next()),o=!0;break}i=!i&&"\\"==r}return(o||!i&&!O)&&(t.tokenize=null),"string"}),t.tokenize(e,t);if(/[\[\]{}\(\),;\\:\?\.]/.test(r))return s=r,"punctuation";if("#"==r)return e.skipToEnd(),"atom";if("%"==r)return e.eatWhile(/\b/),"atom";if(/\d/.test(r))return e.eatWhile(/[\w\.]/),"number";if("/"==r){if(e.eat("*"))return t.tokenize=C,C(e,t);if(e.eat("/"))return e.skipToEnd(),"comment"}if(w.test(r))return"@"==r&&(e.match("try")||e.match("catch")||e.match("lazy"))?"keyword":(e.eatWhile(w),"operator");e.eatWhile(/[\w\$_\xa1-\uffff]/);var i=e.current();return l.propertyIsEnumerable(i)?"keyword":c.propertyIsEnumerable(i)?"builtin":u.propertyIsEnumerable(i)||m.propertyIsEnumerable(i)||f.propertyIsEnumerable(i)||p.propertyIsEnumerable(i)||d.propertyIsEnumerable(i)||b.propertyIsEnumerable(i)?"def":h.propertyIsEnumerable(i)||y.propertyIsEnumerable(i)||v.propertyIsEnumerable(i)?"string":g.propertyIsEnumerable(i)?"typeName.standard":x.propertyIsEnumerable(i)?"modifier":k.propertyIsEnumerable(i)?"atom":"variable"}function C(e,t){for(var n,r=!1;n=e.next();){if("/"==n&&r){t.tokenize=null;break}r="*"==n}return"comment"}function L(e,t,n,r,i){this.indented=e,this.column=t,this.type=n,this.align=r,this.prev=i}function z(e,t,n){var r=e.indented;return e.context&&"statement"==e.context.type&&(r=e.context.indented),e.context=new L(r,t,n,null,e.context)}function T(e){var t=e.context.type;return")"!=t&&"]"!=t&&"}"!=t||(e.indented=e.context.indented),e.context=e.context.prev}const U={name:"ttcn",startState:function(){return{tokenize:null,context:new L(0,0,"top",!1),indented:0,startOfLine:!0}},token:function(e,t){var n=t.context;if(e.sol()&&(null==n.align&&(n.align=!1),t.indented=e.indentation(),t.startOfLine=!0),e.eatSpace())return null;s=null;var r=(t.tokenize||I)(e,t);if("comment"==r)return r;if(null==n.align&&(n.align=!0),";"!=s&&":"!=s&&","!=s||"statement"!=n.type)if("{"==s)z(t,e.column(),"}");else if("["==s)z(t,e.column(),"]");else if("("==s)z(t,e.column(),")");else if("}"==s){for(;"statement"==n.type;)n=T(t);for("}"==n.type&&(n=T(t));"statement"==n.type;)n=T(t)}else s==n.type?T(t):E&&(("}"==n.type||"top"==n.type)&&";"!=s||"statement"==n.type&&"newstatement"==s)&&z(t,e.column(),"statement");else T(t);return t.startOfLine=!1,r},languageData:{indentOnInput:/^\s*[{}]$/,commentTokens:{line:"//",block:{open:"/*",close:"*/"}},autocomplete:o}}}}]);