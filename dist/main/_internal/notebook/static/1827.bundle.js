"use strict";(self.webpackChunk_JUPYTERLAB_CORE_OUTPUT=self.webpackChunk_JUPYTERLAB_CORE_OUTPUT||[]).push([[1827],{41827:(e,t,r)=>{r.r(t),r.d(t,{default:()=>w});var i=r(86883),n=r(56165),o=r(21058),a=r(40930),s=r(80309),d=r(50881),l=r(20457),c=r(49255);const h="CSVTable",u="TSVTable";var g;!function(e){e.CSVGoToLine="csv:go-to-line",e.TSVGoToLine="tsv:go-to-line"}(g||(g={}));const _={activate:function(e,t,i,s,d,l,c,u){const{commands:m,shell:w}=e;let p;u&&(u.addFactory(h,"delimiter",(e=>new a.p({widget:e.content,translator:t}))),c&&(p=(0,n.createToolbarFactory)(u,c,h,_.id,t)));const C=t.load("jupyterlab"),T=new o.LT({name:h,label:C.__("CSV Viewer"),fileTypes:["csv"],defaultFor:["csv"],readOnly:!0,toolbarFactory:p,translator:t}),v=new n.WidgetTracker({namespace:"csvviewer"});let f=y.LIGHT_STYLE,b=y.LIGHT_TEXT_CONFIG;i&&i.restore(v,{command:"docmanager:open",args:e=>({path:e.context.path,factory:h}),name:e=>e.context.path}),e.docRegistry.addWidgetFactory(T);const S=e.docRegistry.getFileType("csv");let L=!1;T.widgetCreated.connect((async(e,t)=>{if(v.add(t),t.context.pathChanged.connect((()=>{v.save(t)})),S&&(t.title.icon=S.icon,t.title.iconClass=S.iconClass,t.title.iconLabel=S.iconLabel),l&&!L){const{CSVSearchProvider:e}=await r.e(6017).then(r.bind(r,36017));l.add("csv",e),L=!0}await t.content.ready,t.content.style=f,t.content.rendererConfig=b}));s&&s.themeChanged.connect((()=>{const e=!s||!s.theme||s.isLight(s.theme);f=e?y.LIGHT_STYLE:y.DARK_STYLE,b=e?y.LIGHT_TEXT_CONFIG:y.DARK_TEXT_CONFIG,v.forEach((async e=>{await e.content.ready,e.content.style=f,e.content.rendererConfig=b}))}));const F=()=>null!==v.currentWidget&&v.currentWidget===w.currentWidget;m.addCommand(g.CSVGoToLine,{label:C.__("Go to Line"),execute:async()=>{const e=v.currentWidget;if(null===e)return;const t=await n.InputDialog.getNumber({title:C.__("Go to Line"),value:0});t.button.accept&&null!==t.value&&e.content.goToLine(t.value)},isEnabled:F}),d&&d.editMenu.goToLiners.add({id:g.CSVGoToLine,isEnabled:F})},id:"@jupyterlab/csvviewer-extension:csv",description:"Adds viewer for CSV file types",requires:[c.ITranslator],optional:[i.ILayoutRestorer,n.IThemeManager,d.IMainMenu,s.ISearchProviderRegistry,l.ISettingRegistry,n.IToolbarWidgetRegistry],autoStart:!0},m={activate:function(e,t,i,s,d,l,c,h){const{commands:_,shell:w}=e;let p;h&&(h.addFactory(u,"delimiter",(e=>new a.p({widget:e.content,translator:t}))),c&&(p=(0,n.createToolbarFactory)(h,c,u,m.id,t)));const C=t.load("jupyterlab"),T=new o._d({name:u,label:C.__("TSV Viewer"),fileTypes:["tsv"],defaultFor:["tsv"],readOnly:!0,toolbarFactory:p,translator:t}),v=new n.WidgetTracker({namespace:"tsvviewer"});let f=y.LIGHT_STYLE,b=y.LIGHT_TEXT_CONFIG;i&&i.restore(v,{command:"docmanager:open",args:e=>({path:e.context.path,factory:u}),name:e=>e.context.path}),e.docRegistry.addWidgetFactory(T);const S=e.docRegistry.getFileType("tsv");let L=!1;T.widgetCreated.connect((async(e,t)=>{if(v.add(t),t.context.pathChanged.connect((()=>{v.save(t)})),S&&(t.title.icon=S.icon,t.title.iconClass=S.iconClass,t.title.iconLabel=S.iconLabel),l&&!L){const{CSVSearchProvider:e}=await r.e(6017).then(r.bind(r,36017));l.add("tsv",e),L=!0}await t.content.ready,t.content.style=f,t.content.rendererConfig=b}));s&&s.themeChanged.connect((()=>{const e=!s||!s.theme||s.isLight(s.theme);f=e?y.LIGHT_STYLE:y.DARK_STYLE,b=e?y.LIGHT_TEXT_CONFIG:y.DARK_TEXT_CONFIG,v.forEach((async e=>{await e.content.ready,e.content.style=f,e.content.rendererConfig=b}))}));const F=()=>null!==v.currentWidget&&v.currentWidget===w.currentWidget;_.addCommand(g.TSVGoToLine,{label:C.__("Go to Line"),execute:async()=>{const e=v.currentWidget;if(null===e)return;const t=await n.InputDialog.getNumber({title:C.__("Go to Line"),value:0});t.button.accept&&null!==t.value&&e.content.goToLine(t.value)},isEnabled:F}),d&&d.editMenu.goToLiners.add({id:g.TSVGoToLine,isEnabled:F})},id:"@jupyterlab/csvviewer-extension:tsv",description:"Adds viewer for TSV file types.",requires:[c.ITranslator],optional:[i.ILayoutRestorer,n.IThemeManager,d.IMainMenu,s.ISearchProviderRegistry,l.ISettingRegistry,n.IToolbarWidgetRegistry],autoStart:!0},w=[_,m];var y;!function(e){e.LIGHT_STYLE={voidColor:"#F3F3F3",backgroundColor:"white",headerBackgroundColor:"#EEEEEE",gridLineColor:"rgba(20, 20, 20, 0.15)",headerGridLineColor:"rgba(20, 20, 20, 0.25)",rowBackgroundColor:e=>e%2==0?"#F5F5F5":"white"},e.DARK_STYLE={voidColor:"black",backgroundColor:"#111111",headerBackgroundColor:"#424242",gridLineColor:"rgba(235, 235, 235, 0.15)",headerGridLineColor:"rgba(235, 235, 235, 0.25)",rowBackgroundColor:e=>e%2==0?"#212121":"#111111"},e.LIGHT_TEXT_CONFIG={textColor:"#111111",matchBackgroundColor:"#FFFFE0",currentMatchBackgroundColor:"#FFFF00",horizontalAlignment:"right"},e.DARK_TEXT_CONFIG={textColor:"#F5F5F5",matchBackgroundColor:"#838423",currentMatchBackgroundColor:"#A3807A",horizontalAlignment:"right"}}(y||(y={}))},40930:(e,t,r)=>{r.d(t,{p:()=>s});var i,n=r(49255),o=r(59361),a=r(9267);class s extends a.Widget{constructor(e){super({node:i.createNode(e.widget.delimiter,e.translator)}),this._widget=e.widget,this.addClass("jp-CSVDelimiter")}get selectNode(){return this.node.getElementsByTagName("select")[0]}handleEvent(e){"change"===e.type&&(this._widget.delimiter=this.selectNode.value)}onAfterAttach(e){this.selectNode.addEventListener("change",this)}onBeforeDetach(e){this.selectNode.removeEventListener("change",this)}}!function(e){e.createNode=function(e,t){const r=null==(t=t||n.nullTranslator)?void 0:t.load("jupyterlab"),i=[[",",","],[";",";"],["\t",r.__("tab")],["|",r.__("pipe")],["#",r.__("hash")]],a=document.createElement("div"),s=document.createElement("span"),d=document.createElement("select");s.textContent=r.__("Delimiter: "),s.className="jp-CSVDelimiter-label";for(const[t,r]of i){const i=document.createElement("option");i.value=t,i.textContent=r,t===e&&(i.selected=!0),d.appendChild(i)}a.appendChild(s);const l=o.Styling.wrapSelect(d);return l.classList.add("jp-CSVDelimiter-dropdown"),a.appendChild(l),a}}(i||(i={}))},21058:(e,t,r)=>{r.d(t,{A9:()=>u,B0:()=>c,JZ:()=>h,LT:()=>_,_d:()=>m,kw:()=>g});var i,n=r(85421),o=r(49358),a=r(20998),s=r(81997),d=r(9267),l=r(40930);class c{}class h{constructor(e){this._looping=!0,this._changed=new s.Signal(this),this._grid=e,this._query=null,this._row=0,this._column=-1}get changed(){return this._changed}cellBackgroundColorRendererFunc(e){return({value:t,row:r,column:i})=>this._query&&t.match(this._query)?this._row===r&&this._column===i?e.currentMatchBackgroundColor:e.matchBackgroundColor:""}clear(){this._query=null,this._row=0,this._column=-1,this._changed.emit(void 0)}find(e,t=!1){const r=this._grid.dataModel,i=r.rowCount("body"),n=r.columnCount("body");this._query!==e&&(this._row=0,this._column=-1),this._query=e;const o=this._grid.scrollY/this._grid.defaultSizes.rowHeight,a=(this._grid.scrollY+this._grid.pageHeight)/this._grid.defaultSizes.rowHeight,s=this._grid.scrollX/this._grid.defaultSizes.columnHeaderHeight,d=(this._grid.scrollX+this._grid.pageWidth)/this._grid.defaultSizes.columnHeaderHeight,l=(e,t)=>e>=o&&e<=a&&t>=s&&t<=d,c=t?-1:1;this._column+=c;for(let o=this._row;t?o>=0:o<i;o+=c){for(let i=this._column;t?i>=0:i<n;i+=c)if(r.data("body",o,i).match(e))return this._changed.emit(void 0),l(o,i)||this._grid.scrollToRow(o),this._row=o,this._column=i,!0;this._column=t?n-1:0}if(this._looping){this._looping=!1,this._row=t?0:i-1,this._wrapRows(t);try{return this.find(e,t)}finally{this._looping=!0}}return!1}_wrapRows(e=!1){const t=this._grid.dataModel,r=t.rowCount("body"),i=t.columnCount("body");e&&this._row<=0?(this._row=r-1,this._column=i):!e&&this._row>=r-1&&(this._row=0,this._column=-1)}get query(){return this._query}}class u extends d.Widget{constructor(e){super(),this._monitor=null,this._delimiter=",",this._revealed=new a.PromiseDelegate,this._baseRenderer=null,this._context=e.context,this.layout=new d.PanelLayout,this.addClass("jp-CSVViewer"),this._ready=this.initialize()}get ready(){return this._ready}async initialize(){const e=this.layout;if(this.isDisposed||!e)return;const{BasicKeyHandler:t,BasicMouseHandler:r,DataGrid:o}=await i.ensureDataGrid();this._defaultStyle=o.defaultStyle,this._grid=new o({defaultSizes:{rowHeight:24,columnWidth:144,rowHeaderWidth:64,columnHeaderHeight:36}}),this._grid.addClass("jp-CSVViewer-grid"),this._grid.headerVisibility="all",this._grid.keyHandler=new t,this._grid.mouseHandler=new r,this._grid.copyConfig={separator:"\t",format:o.copyFormatGeneric,headers:"all",warningThreshold:1e6},e.addWidget(this._grid),this._searchService=new h(this._grid),this._searchService.changed.connect(this._updateRenderer,this),await this._context.ready,await this._updateGrid(),this._revealed.resolve(void 0),this._monitor=new n.ActivityMonitor({signal:this._context.model.contentChanged,timeout:1e3}),this._monitor.activityStopped.connect(this._updateGrid,this)}get context(){return this._context}get revealed(){return this._revealed.promise}get delimiter(){return this._delimiter}set delimiter(e){e!==this._delimiter&&(this._delimiter=e,this._updateGrid())}get style(){return this._grid.style}set style(e){this._grid.style={...this._defaultStyle,...e}}set rendererConfig(e){this._baseRenderer=e,this._updateRenderer()}get searchService(){return this._searchService}dispose(){this._monitor&&this._monitor.dispose(),super.dispose()}goToLine(e){this._grid.scrollToRow(e)}onActivateRequest(e){this.node.tabIndex=-1,this.node.focus()}async _updateGrid(){const{BasicSelectionModel:e}=await i.ensureDataGrid(),{DSVModel:t}=await i.ensureDSVModel(),r=this._context.model.toString(),n=this._delimiter,o=this._grid.dataModel,a=this._grid.dataModel=new t({data:r,delimiter:n});this._grid.selectionModel=new e({dataModel:a}),o&&o.dispose()}async _updateRenderer(){if(null===this._baseRenderer)return;const{TextRenderer:e}=await i.ensureDataGrid(),t=this._baseRenderer,r=new e({textColor:t.textColor,horizontalAlignment:t.horizontalAlignment,backgroundColor:this._searchService.cellBackgroundColorRendererFunc(t)});this._grid.cellRenderers.update({body:r,"column-header":r,"corner-header":r,"row-header":r})}}class g extends o.DocumentWidget{constructor(e){let{content:t,context:r,delimiter:n,reveal:o,...a}=e;t=t||i.createContent(r),o=Promise.all([o,t.revealed]),super({content:t,context:r,reveal:o,...a}),n&&(t.delimiter=n)}setFragment(e){const t=e.split("=");if("#row"!==t[0])return;let r=t[1].split(";")[0];r=r.split("-")[0],this.context.ready.then((()=>{this.content.goToLine(Number(r))}))}}class _ extends o.ABCWidgetFactory{createNewWidget(e){const t=this.translator;return new g({context:e,translator:t})}defaultToolbarFactory(e){return[{name:"delimiter",widget:new l.p({widget:e.content,translator:this.translator})}]}}class m extends _{createNewWidget(e){return new g({context:e,delimiter:"\t",translator:this.translator})}}!function(e){let t=null,i=null;e.ensureDataGrid=async function(){return null==t&&(t=new a.PromiseDelegate,t.resolve(await r.e(1056).then(r.t.bind(r,81056,23)))),t.promise},e.ensureDSVModel=async function(){return null==i&&(i=new a.PromiseDelegate,i.resolve(await Promise.all([r.e(8032),r.e(1056)]).then(r.bind(r,18032)))),i.promise},e.createContent=function(e){return new u({context:e})}}(i||(i={}))}}]);