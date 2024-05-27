"use strict";(self.webpackChunk_JUPYTERLAB_CORE_OUTPUT=self.webpackChunk_JUPYTERLAB_CORE_OUTPUT||[]).push([[5777,5765],{25777:(e,t,n)=>{n.r(t),n.d(t,{Bounce:()=>O,Flip:()=>w,Icons:()=>y,Slide:()=>R,ToastContainer:()=>k,Zoom:()=>N,collapseToast:()=>p,cssTransition:()=>f,toast:()=>S,useToast:()=>C,useToastContainer:()=>v});var o=n(78156),s=n.n(o);function a(e){var t,n,o="";if("string"==typeof e||"number"==typeof e)o+=e;else if("object"==typeof e)if(Array.isArray(e))for(t=0;t<e.length;t++)e[t]&&(n=a(e[t]))&&(o&&(o+=" "),o+=n);else for(t in e)e[t]&&(o&&(o+=" "),o+=t);return o}const r=function(){for(var e,t,n=0,o="";n<arguments.length;)(e=arguments[n++])&&(t=a(e))&&(o&&(o+=" "),o+=t);return o},i=e=>"number"==typeof e&&!isNaN(e),l=e=>"string"==typeof e,c=e=>"function"==typeof e,u=e=>l(e)||c(e)?e:null,d=e=>(0,o.isValidElement)(e)||l(e)||c(e)||i(e);function p(e,t,n){void 0===n&&(n=300);const{scrollHeight:o,style:s}=e;requestAnimationFrame((()=>{s.minHeight="initial",s.height=o+"px",s.transition=`all ${n}ms`,requestAnimationFrame((()=>{s.height="0",s.padding="0",s.margin="0",setTimeout(t,n)}))}))}function f(e){let{enter:t,exit:n,appendPosition:a=!1,collapse:r=!0,collapseDuration:i=300}=e;return function(e){let{children:l,position:c,preventExitTransition:u,done:d,nodeRef:f,isIn:m}=e;const g=a?`${t}--${c}`:t,h=a?`${n}--${c}`:n,y=(0,o.useRef)(0);return(0,o.useLayoutEffect)((()=>{const e=f.current,t=g.split(" "),n=o=>{o.target===f.current&&(e.dispatchEvent(new Event("d")),e.removeEventListener("animationend",n),e.removeEventListener("animationcancel",n),0===y.current&&"animationcancel"!==o.type&&e.classList.remove(...t))};e.classList.add(...t),e.addEventListener("animationend",n),e.addEventListener("animationcancel",n)}),[]),(0,o.useEffect)((()=>{const e=f.current,t=()=>{e.removeEventListener("animationend",t),r?p(e,d,i):d()};m||(u?t():(y.current=1,e.className+=` ${h}`,e.addEventListener("animationend",t)))}),[m]),s().createElement(s().Fragment,null,l)}}function m(e,t){return null!=e?{content:e.content,containerId:e.props.containerId,id:e.props.toastId,theme:e.props.theme,type:e.props.type,data:e.props.data||{},isLoading:e.props.isLoading,icon:e.props.icon,status:t}:{}}const g={list:new Map,emitQueue:new Map,on(e,t){return this.list.has(e)||this.list.set(e,[]),this.list.get(e).push(t),this},off(e,t){if(t){const n=this.list.get(e).filter((e=>e!==t));return this.list.set(e,n),this}return this.list.delete(e),this},cancelEmit(e){const t=this.emitQueue.get(e);return t&&(t.forEach(clearTimeout),this.emitQueue.delete(e)),this},emit(e){this.list.has(e)&&this.list.get(e).forEach((t=>{const n=setTimeout((()=>{t(...[].slice.call(arguments,1))}),0);this.emitQueue.has(e)||this.emitQueue.set(e,[]),this.emitQueue.get(e).push(n)}))}},h=e=>{let{theme:t,type:n,...o}=e;return s().createElement("svg",{viewBox:"0 0 24 24",width:"100%",height:"100%",fill:"colored"===t?"currentColor":`var(--toastify-icon-color-${n})`,...o})},y={info:function(e){return s().createElement(h,{...e},s().createElement("path",{d:"M12 0a12 12 0 1012 12A12.013 12.013 0 0012 0zm.25 5a1.5 1.5 0 11-1.5 1.5 1.5 1.5 0 011.5-1.5zm2.25 13.5h-4a1 1 0 010-2h.75a.25.25 0 00.25-.25v-4.5a.25.25 0 00-.25-.25h-.75a1 1 0 010-2h1a2 2 0 012 2v4.75a.25.25 0 00.25.25h.75a1 1 0 110 2z"}))},warning:function(e){return s().createElement(h,{...e},s().createElement("path",{d:"M23.32 17.191L15.438 2.184C14.728.833 13.416 0 11.996 0c-1.42 0-2.733.833-3.443 2.184L.533 17.448a4.744 4.744 0 000 4.368C1.243 23.167 2.555 24 3.975 24h16.05C22.22 24 24 22.044 24 19.632c0-.904-.251-1.746-.68-2.44zm-9.622 1.46c0 1.033-.724 1.823-1.698 1.823s-1.698-.79-1.698-1.822v-.043c0-1.028.724-1.822 1.698-1.822s1.698.79 1.698 1.822v.043zm.039-12.285l-.84 8.06c-.057.581-.408.943-.897.943-.49 0-.84-.367-.896-.942l-.84-8.065c-.057-.624.25-1.095.779-1.095h1.91c.528.005.84.476.784 1.1z"}))},success:function(e){return s().createElement(h,{...e},s().createElement("path",{d:"M12 0a12 12 0 1012 12A12.014 12.014 0 0012 0zm6.927 8.2l-6.845 9.289a1.011 1.011 0 01-1.43.188l-4.888-3.908a1 1 0 111.25-1.562l4.076 3.261 6.227-8.451a1 1 0 111.61 1.183z"}))},error:function(e){return s().createElement(h,{...e},s().createElement("path",{d:"M11.983 0a12.206 12.206 0 00-8.51 3.653A11.8 11.8 0 000 12.207 11.779 11.779 0 0011.8 24h.214A12.111 12.111 0 0024 11.791 11.766 11.766 0 0011.983 0zM10.5 16.542a1.476 1.476 0 011.449-1.53h.027a1.527 1.527 0 011.523 1.47 1.475 1.475 0 01-1.449 1.53h-.027a1.529 1.529 0 01-1.523-1.47zM11 12.5v-6a1 1 0 012 0v6a1 1 0 11-2 0z"}))},spinner:function(){return s().createElement("div",{className:"Toastify__spinner"})}};function v(e){const[,t]=(0,o.useReducer)((e=>e+1),0),[n,s]=(0,o.useState)([]),a=(0,o.useRef)(null),r=(0,o.useRef)(new Map).current,p=e=>-1!==n.indexOf(e),f=(0,o.useRef)({toastKey:1,displayedToast:0,count:0,queue:[],props:e,containerId:null,isToastActive:p,getToast:e=>r.get(e)}).current;function h(e){let{containerId:t}=e;const{limit:n}=f.props;!n||t&&f.containerId!==t||(f.count-=f.queue.length,f.queue=[])}function v(e){s((t=>null==e?[]:t.filter((t=>t!==e))))}function T(){const{toastContent:e,toastProps:t,staleId:n}=f.queue.shift();C(e,t,n)}function E(e,n){let{delay:s,staleId:p,...h}=n;if(!d(e)||function(e){return!a.current||f.props.enableMultiContainer&&e.containerId!==f.props.containerId||r.has(e.toastId)&&null==e.updateId}(h))return;const{toastId:E,updateId:b,data:_}=h,{props:I}=f,L=()=>v(E),O=null==b;O&&f.count++;const R={...I,style:I.toastStyle,key:f.toastKey++,...Object.fromEntries(Object.entries(h).filter((e=>{let[t,n]=e;return null!=n}))),toastId:E,updateId:b,data:_,closeToast:L,isIn:!1,className:u(h.className||I.toastClassName),bodyClassName:u(h.bodyClassName||I.bodyClassName),progressClassName:u(h.progressClassName||I.progressClassName),autoClose:!h.isLoading&&(N=h.autoClose,w=I.autoClose,!1===N||i(N)&&N>0?N:w),deleteToast(){const e=m(r.get(E),"removed");r.delete(E),g.emit(4,e);const n=f.queue.length;if(f.count=null==E?f.count-f.displayedToast:f.count-1,f.count<0&&(f.count=0),n>0){const e=null==E?f.props.limit:1;if(1===n||1===e)f.displayedToast++,T();else{const t=e>n?n:e;f.displayedToast=t;for(let e=0;e<t;e++)T()}}else t()}};var N,w;R.iconOut=function(e){let{theme:t,type:n,isLoading:s,icon:a}=e,r=null;const u={theme:t,type:n};return!1===a||(c(a)?r=a(u):(0,o.isValidElement)(a)?r=(0,o.cloneElement)(a,u):l(a)||i(a)?r=a:s?r=y.spinner():(e=>e in y)(n)&&(r=y[n](u))),r}(R),c(h.onOpen)&&(R.onOpen=h.onOpen),c(h.onClose)&&(R.onClose=h.onClose),R.closeButton=I.closeButton,!1===h.closeButton||d(h.closeButton)?R.closeButton=h.closeButton:!0===h.closeButton&&(R.closeButton=!d(I.closeButton)||I.closeButton);let k=e;(0,o.isValidElement)(e)&&!l(e.type)?k=(0,o.cloneElement)(e,{closeToast:L,toastProps:R,data:_}):c(e)&&(k=e({closeToast:L,toastProps:R,data:_})),I.limit&&I.limit>0&&f.count>I.limit&&O?f.queue.push({toastContent:k,toastProps:R,staleId:p}):i(s)?setTimeout((()=>{C(k,R,p)}),s):C(k,R,p)}function C(e,t,n){const{toastId:o}=t;n&&r.delete(n);const a={content:e,props:t};r.set(o,a),s((e=>[...e,o].filter((e=>e!==n)))),g.emit(4,m(a,null==a.props.updateId?"added":"updated"))}return(0,o.useEffect)((()=>(f.containerId=e.containerId,g.cancelEmit(3).on(0,E).on(1,(e=>a.current&&v(e))).on(5,h).emit(2,f),()=>{r.clear(),g.emit(3,f)})),[]),(0,o.useEffect)((()=>{f.props=e,f.isToastActive=p,f.displayedToast=n.length})),{getToastToRender:function(t){const n=new Map,o=Array.from(r.values());return e.newestOnTop&&o.reverse(),o.forEach((e=>{const{position:t}=e.props;n.has(t)||n.set(t,[]),n.get(t).push(e)})),Array.from(n,(e=>t(e[0],e[1])))},containerRef:a,isToastActive:p}}function T(e){return e.targetTouches&&e.targetTouches.length>=1?e.targetTouches[0].clientX:e.clientX}function E(e){return e.targetTouches&&e.targetTouches.length>=1?e.targetTouches[0].clientY:e.clientY}function C(e){const[t,n]=(0,o.useState)(!1),[s,a]=(0,o.useState)(!1),r=(0,o.useRef)(null),i=(0,o.useRef)({start:0,x:0,y:0,delta:0,removalDistance:0,canCloseOnClick:!0,canDrag:!1,boundingRect:null,didMove:!1}).current,l=(0,o.useRef)(e),{autoClose:u,pauseOnHover:d,closeToast:p,onClick:f,closeOnClick:m}=e;function g(t){if(e.draggable){"touchstart"===t.nativeEvent.type&&t.nativeEvent.preventDefault(),i.didMove=!1,document.addEventListener("mousemove",C),document.addEventListener("mouseup",b),document.addEventListener("touchmove",C),document.addEventListener("touchend",b);const n=r.current;i.canCloseOnClick=!0,i.canDrag=!0,i.boundingRect=n.getBoundingClientRect(),n.style.transition="",i.x=T(t.nativeEvent),i.y=E(t.nativeEvent),"x"===e.draggableDirection?(i.start=i.x,i.removalDistance=n.offsetWidth*(e.draggablePercent/100)):(i.start=i.y,i.removalDistance=n.offsetHeight*(80===e.draggablePercent?1.5*e.draggablePercent:e.draggablePercent/100))}}function h(t){if(i.boundingRect){const{top:n,bottom:o,left:s,right:a}=i.boundingRect;"touchend"!==t.nativeEvent.type&&e.pauseOnHover&&i.x>=s&&i.x<=a&&i.y>=n&&i.y<=o?v():y()}}function y(){n(!0)}function v(){n(!1)}function C(n){const o=r.current;i.canDrag&&o&&(i.didMove=!0,t&&v(),i.x=T(n),i.y=E(n),i.delta="x"===e.draggableDirection?i.x-i.start:i.y-i.start,i.start!==i.x&&(i.canCloseOnClick=!1),o.style.transform=`translate${e.draggableDirection}(${i.delta}px)`,o.style.opacity=""+(1-Math.abs(i.delta/i.removalDistance)))}function b(){document.removeEventListener("mousemove",C),document.removeEventListener("mouseup",b),document.removeEventListener("touchmove",C),document.removeEventListener("touchend",b);const t=r.current;if(i.canDrag&&i.didMove&&t){if(i.canDrag=!1,Math.abs(i.delta)>i.removalDistance)return a(!0),void e.closeToast();t.style.transition="transform 0.2s, opacity 0.2s",t.style.transform=`translate${e.draggableDirection}(0)`,t.style.opacity="1"}}(0,o.useEffect)((()=>{l.current=e})),(0,o.useEffect)((()=>(r.current&&r.current.addEventListener("d",y,{once:!0}),c(e.onOpen)&&e.onOpen((0,o.isValidElement)(e.children)&&e.children.props),()=>{const e=l.current;c(e.onClose)&&e.onClose((0,o.isValidElement)(e.children)&&e.children.props)})),[]),(0,o.useEffect)((()=>(e.pauseOnFocusLoss&&(document.hasFocus()||v(),window.addEventListener("focus",y),window.addEventListener("blur",v)),()=>{e.pauseOnFocusLoss&&(window.removeEventListener("focus",y),window.removeEventListener("blur",v))})),[e.pauseOnFocusLoss]);const _={onMouseDown:g,onTouchStart:g,onMouseUp:h,onTouchEnd:h};return u&&d&&(_.onMouseEnter=v,_.onMouseLeave=y),m&&(_.onClick=e=>{f&&f(e),i.canCloseOnClick&&p()}),{playToast:y,pauseToast:v,isRunning:t,preventExitTransition:s,toastRef:r,eventHandlers:_}}function b(e){let{closeToast:t,theme:n,ariaLabel:o="close"}=e;return s().createElement("button",{className:`Toastify__close-button Toastify__close-button--${n}`,type:"button",onClick:e=>{e.stopPropagation(),t(e)},"aria-label":o},s().createElement("svg",{"aria-hidden":"true",viewBox:"0 0 14 16"},s().createElement("path",{fillRule:"evenodd",d:"M7.71 8.23l3.75 3.75-1.48 1.48-3.75-3.75-3.75 3.75L1 11.98l3.75-3.75L1 4.48 2.48 3l3.75 3.75L9.98 3l1.48 1.48-3.75 3.75z"})))}function _(e){let{delay:t,isRunning:n,closeToast:o,type:a="default",hide:i,className:l,style:u,controlledProgress:d,progress:p,rtl:f,isIn:m,theme:g}=e;const h=i||d&&0===p,y={...u,animationDuration:`${t}ms`,animationPlayState:n?"running":"paused",opacity:h?0:1};d&&(y.transform=`scaleX(${p})`);const v=r("Toastify__progress-bar",d?"Toastify__progress-bar--controlled":"Toastify__progress-bar--animated",`Toastify__progress-bar-theme--${g}`,`Toastify__progress-bar--${a}`,{"Toastify__progress-bar--rtl":f}),T=c(l)?l({rtl:f,type:a,defaultClassName:v}):r(v,l);return s().createElement("div",{role:"progressbar","aria-hidden":h?"true":"false","aria-label":"notification timer",className:T,style:y,[d&&p>=1?"onTransitionEnd":"onAnimationEnd"]:d&&p<1?null:()=>{m&&o()}})}const I=e=>{const{isRunning:t,preventExitTransition:n,toastRef:a,eventHandlers:i}=C(e),{closeButton:l,children:u,autoClose:d,onClick:p,type:f,hideProgressBar:m,closeToast:g,transition:h,position:y,className:v,style:T,bodyClassName:E,bodyStyle:I,progressClassName:L,progressStyle:O,updateId:R,role:N,progress:w,rtl:k,toastId:M,deleteToast:P,isIn:B,isLoading:x,iconOut:$,closeOnClick:A,theme:D}=e,z=r("Toastify__toast",`Toastify__toast-theme--${D}`,`Toastify__toast--${f}`,{"Toastify__toast--rtl":k},{"Toastify__toast--close-on-click":A}),F=c(v)?v({rtl:k,position:y,type:f,defaultClassName:z}):r(z,v),S=!!w||!d,H={closeToast:g,type:f,theme:D};let U=null;return!1===l||(U=c(l)?l(H):(0,o.isValidElement)(l)?(0,o.cloneElement)(l,H):b(H)),s().createElement(h,{isIn:B,done:P,position:y,preventExitTransition:n,nodeRef:a},s().createElement("div",{id:M,onClick:p,className:F,...i,style:T,ref:a},s().createElement("div",{...B&&{role:N},className:c(E)?E({type:f}):r("Toastify__toast-body",E),style:I},null!=$&&s().createElement("div",{className:r("Toastify__toast-icon",{"Toastify--animate-icon Toastify__zoom-enter":!x})},$),s().createElement("div",null,u)),U,s().createElement(_,{...R&&!S?{key:`pb-${R}`}:{},rtl:k,theme:D,delay:d,isRunning:t,isIn:B,closeToast:g,hide:m,type:f,style:O,className:L,controlledProgress:S,progress:w||0})))},L=function(e,t){return void 0===t&&(t=!1),{enter:`Toastify--animate Toastify__${e}-enter`,exit:`Toastify--animate Toastify__${e}-exit`,appendPosition:t}},O=f(L("bounce",!0)),R=f(L("slide",!0)),N=f(L("zoom")),w=f(L("flip")),k=(0,o.forwardRef)(((e,t)=>{const{getToastToRender:n,containerRef:a,isToastActive:i}=v(e),{className:l,style:d,rtl:p,containerId:f}=e;function m(e){const t=r("Toastify__toast-container",`Toastify__toast-container--${e}`,{"Toastify__toast-container--rtl":p});return c(l)?l({position:e,rtl:p,defaultClassName:t}):r(t,u(l))}return(0,o.useEffect)((()=>{t&&(t.current=a.current)}),[]),s().createElement("div",{ref:a,className:"Toastify",id:f},n(((e,t)=>{const n=t.length?{...d}:{...d,pointerEvents:"none"};return s().createElement("div",{className:m(e),style:n,key:`container-${e}`},t.map(((e,n)=>{let{content:o,props:a}=e;return s().createElement(I,{...a,isIn:i(a.toastId),style:{...a.style,"--nth":n+1,"--len":t.length},key:`toast-${a.key}`},o)})))})))}));k.displayName="ToastContainer",k.defaultProps={position:"top-right",transition:O,autoClose:5e3,closeButton:b,pauseOnHover:!0,pauseOnFocusLoss:!0,closeOnClick:!0,draggable:!0,draggablePercent:80,draggableDirection:"x",role:"alert",theme:"light"};let M,P=new Map,B=[],x=1;function $(){return""+x++}function A(e){return e&&(l(e.toastId)||i(e.toastId))?e.toastId:$()}function D(e,t){return P.size>0?g.emit(0,e,t):B.push({content:e,options:t}),t.toastId}function z(e,t){return{...t,type:t&&t.type||e,toastId:A(t)}}function F(e){return(t,n)=>D(t,z(e,n))}function S(e,t){return D(e,z("default",t))}S.loading=(e,t)=>D(e,z("default",{isLoading:!0,autoClose:!1,closeOnClick:!1,closeButton:!1,draggable:!1,...t})),S.promise=function(e,t,n){let o,{pending:s,error:a,success:r}=t;s&&(o=l(s)?S.loading(s,n):S.loading(s.render,{...n,...s}));const i={isLoading:null,autoClose:null,closeOnClick:null,closeButton:null,draggable:null},u=(e,t,s)=>{if(null==t)return void S.dismiss(o);const a={type:e,...i,...n,data:s},r=l(t)?{render:t}:t;return o?S.update(o,{...a,...r}):S(r.render,{...a,...r}),s},d=c(e)?e():e;return d.then((e=>u("success",r,e))).catch((e=>u("error",a,e))),d},S.success=F("success"),S.info=F("info"),S.error=F("error"),S.warning=F("warning"),S.warn=S.warning,S.dark=(e,t)=>D(e,z("default",{theme:"dark",...t})),S.dismiss=e=>{P.size>0?g.emit(1,e):B=B.filter((t=>null!=e&&t.options.toastId!==e))},S.clearWaitingQueue=function(e){return void 0===e&&(e={}),g.emit(5,e)},S.isActive=e=>{let t=!1;return P.forEach((n=>{n.isToastActive&&n.isToastActive(e)&&(t=!0)})),t},S.update=function(e,t){void 0===t&&(t={}),setTimeout((()=>{const n=function(e,t){let{containerId:n}=t;const o=P.get(n||M);return o&&o.getToast(e)}(e,t);if(n){const{props:o,content:s}=n,a={delay:100,...o,...t,toastId:t.toastId||e,updateId:$()};a.toastId!==e&&(a.staleId=e);const r=a.render||s;delete a.render,D(r,a)}}),0)},S.done=e=>{S.update(e,{progress:1})},S.onChange=e=>(g.on(4,e),()=>{g.off(4,e)}),S.POSITION={TOP_LEFT:"top-left",TOP_RIGHT:"top-right",TOP_CENTER:"top-center",BOTTOM_LEFT:"bottom-left",BOTTOM_RIGHT:"bottom-right",BOTTOM_CENTER:"bottom-center"},S.TYPE={INFO:"info",SUCCESS:"success",WARNING:"warning",ERROR:"error",DEFAULT:"default"},g.on(2,(e=>{M=e.containerId||e,P.set(M,e),B.forEach((e=>{g.emit(0,e.content,e.options)})),B=[]})).on(3,(e=>{P.delete(e.containerId||e),0===P.size&&g.off(0).off(1).off(5)}))}}]);