"use strict";(self.webpackChunk_JUPYTERLAB_CORE_OUTPUT=self.webpackChunk_JUPYTERLAB_CORE_OUTPUT||[]).push([[6027,5573],{5573:(e,t,o)=>{o.r(t),o.d(t,{default:()=>E});var n=o(56165),a=o(85421),s=o(89488),r=o(50881),c=o(44148),l=o(20457),i=o(49255),d=o(16882),u=o(97934),k=o(9267),b=o(78156),p=o.n(b);const g=e=>{const t=e.model;if(!t)return!1;const o=Array.from(t.cells);let n=0,a=0;for(const e of o)"code"===e.type&&(n++,e.trusted&&a++);return a===n},h=({notebook:e,translator:t})=>{const o=t.load("notebook"),[n,a]=(0,b.useState)(g(e)),s=()=>{const t=g(e);a(t)};return(0,b.useEffect)((()=>(e.modelContentChanged.connect(s),e.activeCellChanged.connect(s),s(),()=>{e.modelContentChanged.disconnect(s),e.activeCellChanged.disconnect(s)}))),p().createElement("button",{className:"jp-NotebookTrustedStatus",style:n?{cursor:"help"}:{cursor:"pointer"},onClick:()=>!n&&(async()=>{await c.NotebookActions.trust(e,t),s()})(),title:n?o.__("JavaScript enabled for notebook display"):o.__("JavaScript disabled for notebook display")},n?o.__("Trusted"):o.__("Not Trusted"))};var C;!function(e){e.create=({notebook:e,translator:t})=>n.ReactWidget.create(p().createElement(h,{notebook:e,translator:t}))}(C||(C={}));const f="jp-NotebookKernelStatus-error",m="jp-NotebookKernelStatus-warn",v="jp-NotebookKernelStatus-info",y="jp-NotebookKernelStatus-fade",S={id:"@jupyter-notebook/notebook-extension:checkpoints",autoStart:!0,requires:[s.IDocumentManager,i.ITranslator],optional:[d.INotebookShell,n.IToolbarWidgetRegistry],activate:(e,t,o,s,r)=>{const{shell:c}=e,l=o.load("notebook"),i=document.createElement("div");r&&r.addFactory("TopBar","checkpoint",(e=>{const t=new k.Widget({node:i});return t.id=n.DOMUtils.createDomID(),t.addClass("jp-NotebookCheckpoint"),t}));const d=async()=>{const e=c.currentWidget;if(!e)return;const o=t.contextForWidget(e);null==o||o.fileChanged.disconnect(d),null==o||o.fileChanged.connect(d);const n=await(null==o?void 0:o.listCheckpoints());if(!n)return;const s=n[n.length-1];i.textContent=l.__("Last Checkpoint: %1",a.Time.formatHuman(new Date(s.last_modified)))};s&&s.currentChanged.connect(d),new u.Poll({auto:!0,factory:()=>d(),frequency:{interval:2e3,backoff:!1},standby:"when-hidden"})}},N={id:"@jupyter-notebook/notebook-extension:close-tab",autoStart:!0,requires:[r.IMainMenu],optional:[i.ITranslator],activate:(e,t,o)=>{const{commands:n}=e,a=(o=null!=o?o:i.nullTranslator).load("notebook"),s="notebook:close-and-halt";n.addCommand(s,{label:a.__("Close and Shut Down Notebook"),execute:async()=>{await n.execute("notebook:close-and-shutdown"),window.close()}}),t.fileMenu.closeAndCleaners.add({id:s,rank:0})}},x={id:"@jupyter-notebook/notebook-extension:kernel-logo",autoStart:!0,requires:[d.INotebookShell],optional:[n.IToolbarWidgetRegistry],activate:(e,t,o)=>{const{serviceManager:n}=e,a=document.createElement("div"),s=document.createElement("img"),r=async()=>{var e,o,l,i,d;const u=t.currentWidget;if(!(u instanceof c.NotebookPanel))return;a.hasChildNodes()||a.appendChild(s),await u.sessionContext.ready,u.sessionContext.kernelChanged.disconnect(r),u.sessionContext.kernelChanged.connect(r);const k=null!==(l=null===(o=null===(e=u.sessionContext.session)||void 0===e?void 0:e.kernel)||void 0===o?void 0:o.name)&&void 0!==l?l:"",b=null===(d=null===(i=n.kernelspecs)||void 0===i?void 0:i.specs)||void 0===d?void 0:d.kernelspecs[k];if(!b)return void a.childNodes[0].remove();const p=b.resources["logo-64x64"];p?(s.src=p,s.title=b.display_name):a.childNodes[0].remove()};o&&o.addFactory("TopBar","kernelLogo",(e=>{const t=new k.Widget({node:a});return t.addClass("jp-NotebookKernelLogo"),t})),e.started.then((()=>{t.currentChanged.connect(r)}))}},w={id:"@jupyter-notebook/notebook-extension:kernel-status",autoStart:!0,requires:[d.INotebookShell,i.ITranslator],activate:(e,t,o)=>{const n=o.load("notebook"),s=new k.Widget;s.addClass("jp-NotebookKernelStatus"),e.shell.add(s,"menu",{rank:10010});const r=e=>{const t=e.kernelDisplayStatus;let o=`Kernel ${a.Text.titleCase(t)}`;switch(s.removeClass(f),s.removeClass(m),s.removeClass(v),s.removeClass(y),t){case"busy":case"idle":o="",s.addClass(y);break;case"dead":case"terminating":s.addClass(f);break;case"unknown":s.addClass(m);break;default:s.addClass(v),s.addClass(y)}s.node.textContent=n.__(o)};t.currentChanged.connect((async()=>{const e=t.currentWidget;e instanceof c.NotebookPanel&&e.sessionContext.statusChanged.connect(r)}))}},T={id:"@jupyter-notebook/notebook-extension:scroll-output",autoStart:!0,requires:[c.INotebookTracker],optional:[l.ISettingRegistry],activate:async(e,t,o)=>{let n=!0;const a=e=>{if(!n)return;const{outputArea:t}=e;if(void 0!==e.model.getMetadata("scrolled"))return;const{node:o}=t,a=o.scrollHeight>1.3*(parseFloat(o.style.fontSize.replace("px",""))||14)*100;e.toggleClass("jp-mod-outputsScrolled",a)},s={},r=e=>{if("code"===e.model.type){const t=e,o=t.model.id;a(t),s[o]&&t.outputArea.model.changed.disconnect(s[o]),s[o]=()=>a(t),t.outputArea.model.changed.connect(s[o])}};if(t.widgetAdded.connect(((e,t)=>{var o;t.sessionContext.ready.then((()=>{t.content.widgets.forEach(r)})),null===(o=t.model)||void 0===o||o.cells.changed.connect(((e,o)=>{t.content.widgets.forEach(r)}))})),o){const t=o.load(T.id),a=e=>{n=e.get("autoScrollOutputs").composite};Promise.all([t,e.restored]).then((([e])=>{a(e),e.changed.connect((e=>{a(e)}))})).catch((e=>{console.error(e.message)}))}}},_={id:"@jupyter-notebook/notebook-extension:notebook-tools",autoStart:!0,requires:[d.INotebookShell],optional:[c.INotebookTools],activate:(e,t,o)=>{t.currentChanged.connect((async()=>{t.currentWidget instanceof c.NotebookPanel&&o&&t.add(o,"right",{type:"Property Inspector"})}))}},j={id:"@jupyter-notebook/notebook-extension:tab-icon",autoStart:!0,requires:[c.INotebookTracker],activate:(e,t)=>{const o=a.PageConfig.getBaseUrl(),n=a.URLExt.join(o,"static/favicons/favicon-notebook.ico"),s=a.URLExt.join(o,"static/favicons/favicon-busy-1.ico");t.currentChanged.connect((async()=>{const e=t.currentWidget,o=null==e?void 0:e.sessionContext;o&&o.statusChanged.connect((()=>{(e=>{const t=document.querySelector("link[rel*='icon']");switch(e){case"busy":t.href=s;break;case"idle":t.href=n}})(o.kernelDisplayStatus)}))}))}},I={id:"@jupyter-notebook/notebook-extension:trusted",autoStart:!0,requires:[d.INotebookShell,i.ITranslator],activate:(e,t,o)=>{t.currentChanged.connect((async()=>{const e=t.currentWidget;if(!(e instanceof c.NotebookPanel))return;const n=e.content;await e.context.ready;const a=C.create({notebook:n,translator:o});t.add(a,"menu",{rank:11e3})}))}},E=[S,N,x,w,_,T,j,I]}}]);