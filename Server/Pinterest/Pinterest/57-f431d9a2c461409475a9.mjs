(window.__LOADABLE_LOADED_CHUNKS__=window.__LOADABLE_LOADED_CHUNKS__||[]).push([[57],{"+lzj":function(t,e,n){n.d(e,"a",(function(){return c})),n.d(e,"b",(function(){return s})),n.d(e,"c",(function(){return u}));var a=n("vzKb"),r=n("3/Bf"),i=n("ONNR");const o={cumulativeLayoutShiftScore:0,firstInputDelay:null,longTaskDurations:[],largestContentfulPaint:null},c=()=>{o.longTaskDurations=[]},s=()=>o,u=t=>{let e=0;const n=({name:n,value:a})=>{"CLS"===n?Object(r.e)(t,n,100*a):("LCP"===n&&Object(r.e)(t,"LCPCount",e),Object(r.e)(t,n,a))};Object(a.a)({entryTypes:["longtask"]},t=>{t.getEntries().map(t=>o.longTaskDurations.push(t.duration))},()=>c()),Object(a.a)({type:"first-input",buffered:!0},(t,e)=>{const n=t.getEntries()[0];n&&n.startTime&&n.processingStart&&(o.firstInputDelay={startTime:n.startTime,endTime:n.processingStart}),e.disconnect()},()=>{o.firstInputDelay=null}),Object(a.a)({type:"largest-contentful-paint",buffered:!0},t=>{const n=t.getEntries(),a=n.length,r=n[a-1];r&&(e=a,o.largestContentfulPaint=r.renderTime||r.loadTime||null)}),Object(a.a)({type:"layout-shift",buffered:!0},t=>{t.getEntries().forEach(t=>{t.hadRecentInput||(o.cumulativeLayoutShiftScore+=t.value)})}),Object(i.c)(n),Object(i.d)(n),Object(i.a)(n),Object(i.b)(n)}},"3R0Q":function(t,e,n){e.a=t=>{const e={};t.forEach(({label:t,timestamp:n})=>{e[t]=(e[t]||[]).concat([n])});const n={};return Object.keys(e).forEach(t=>{(e[t]||[]).forEach((e,a)=>{n[a?`${t}_${a+1}`:t]=e})}),n}},"B/lV":function(t,e,n){const a=t=>{const e=t.replace(new RegExp("^"+(window.location.origin||"")),""),n=document&&document.querySelector(`head > script[src='${e}']`);return!!n&&n.hasAttribute("defer")},r=t=>["pinimg","pinterest","pinterdev"].every(e=>!t.includes(e+".com/"));e.a=(t,e)=>{const n=(({name:t,initiatorType:e})=>{switch(e){case"xmlhttprequest":return"xmlhttprequest";case"img":return"image";case"video":return"video";default:{const e=t.split("."),n=(e.length>1&&e.pop()||"").toLowerCase();return["js","mjs"].includes(n)?"script":"css"===n?"css":["mp4","m4v","mov"].includes(n)?"video":["bmp","gif","jpg","jpeg","png","tiff","webp","svg"].includes(n)?"image":"other"}}})(t),{name:i}=t;return{category:n,isDeferred:"script"===n&&a(i),isExternal:r(i),isVisuallyCompleteRequired:"image"===n&&e.includes(i),timing:t}}},CP5N:function(t,e,n){var a=n("q1tI"),r=n("3R0Q"),i=n("B/lV"),o=n("vzKb"),c=n("FylZ"),s=n("mRg4"),u=n("LvPn"),p=n("XtwW"),d=n("LrH5"),m=n("fZG9"),l=n("xfna"),b=n("3/Bf");const f=Object(d.a)("PwtStopwatch"),y=(t,e)=>{if(p.a){if("start"===e.type&&!t.isTiming){const{name:n,startTime:a,isAuth:r,navigationType:i}=e,o=void 0!==r&&{tags:{isAuth:r}}||void 0;return Object(b.c)("TIMING."+n,o),{isTiming:!0,isSampled:e.isSampled,startTime:"number"==typeof a?a:p.a.now(),metricId:{type:"stopwatch",name:n,navigationType:i},pwtStaticContext:e.pwtStaticContext,annotations:t.annotations,binaryAnnotations:t.binaryAnnotations,spans:t.spans,isAuth:r,traceId:t.traceId}}if("annotate"===e.type){const n=p.a.now();return f(`adding annotation {${e.label}: ${n}}`),{...t,annotations:t.annotations.concat([{label:e.label,timestamp:n}])}}if("binaryAnnotate"===e.type)return f(`adding binary annotation {${e.name}: ${String(e.value)}}`),{...t,binaryAnnotations:{...t.binaryAnnotations,[e.name]:{value:e.value,type:e.annotationType}}};if("binaryAnnotateOperation"===e.type){const{value:n,type:a}=e.binaryAnnotationValueAndType;if(t.binaryAnnotations[e.name]){const r=t.binaryAnnotations[e.name].value||0;return f(`operating on binary annotation {\n          name: ${e.name}\n          pervious value: ${String(r)}\n          operand: ${String(n)}\n        }`),{...t,binaryAnnotations:{...t.binaryAnnotations,[e.name]:{value:n?e.operation(r,n):r,type:a}}}}return{...t,binaryAnnotations:{...t.binaryAnnotations,[e.name]:{value:n,type:a}}}}if("addSubspan"===e.type){f(`adding subspan {${e.name}}`);let n=0;return e.startTime?n=e.startTime:t.startTime?n=t.startTime:f(`WARNING: adding subspan {${e.name}} without start time`),{...t,spans:[...t.spans,{name:e.name,id:Object(c.a)(),startTime:n,endTime:e.endTime,annotationMap:{...e.annotations},binaryAnnotationMap:{...e.binaryAnnotations},parentId:e.parentId}]}}if("subspanStart"===e.type)return f(`starting subspan {${e.name}}`),{...t,spans:[...t.spans,{name:e.name,id:e.id||Object(c.a)(),parentId:e.parentId||null,startTime:p.a.now(),endTime:1/0,annotationMap:{...e.annotations},binaryAnnotationMap:{...e.binaryAnnotations}}]};if("subspanStop"===e.type){f(`stopping subspan {${e.name}}`);const n=t.spans.findIndex(t=>t.name===e.name);return n>-1?(t.spans[n].endTime=p.a.now(),e.annotations&&(t.spans[n].annotationMap={...t.spans[n].annotationMap,...e.annotations}),e.binaryAnnotations&&(t.spans[n].binaryAnnotationMap={...t.spans[n].binaryAnnotationMap,...e.binaryAnnotations})):Object(b.b)("invalid_subspan_stop_name",{name:e.name}),t}if("stop"===e.type&&t.isTiming){const{startTime:n,metricId:a,pwtStaticContext:o,annotations:d,binaryAnnotations:l,isSampled:b,isAuth:f,spans:y,traceId:O}=t;if(e.stopwatchPerformanceObserver&&e.stopwatchPerformanceObserver.disconnect(),b){const t=e.stopTime||p.a.now(),b=[...y.map(e=>(e.endTime===1/0&&(e.endTime=t),e))];if(e.manualAndResourceSpans||0===y.length){const a=Object(c.a)();b.push({name:"network_resources",id:a,startTime:n,endTime:t,annotationMap:{},binaryAnnotationMap:{},parentId:null},...(e.customStopwatchBuffer||[]).map(t=>Object(u.a)(Object(i.a)(t,[]),a)).filter(Boolean))}const v={type:"COMPLETE",traceId:O,startTime:n,endTime:t,spans:b,annotationMap:Object(r.a)(d),binaryAnnotationMap:Object(m.a)({metricId:a,pwtStaticContext:o,binaryAnnotations:l,performanceResourceTimings:e.customStopwatchBuffer||[]})};Object(s.a)({metricId:a,pwtStaticContext:o,result:v,isAuth:f})}return{isTiming:!1,annotations:[],binaryAnnotations:{},spans:[],traceId:Object(c.a)()}}if("error"===e.type){const{error:t,stopwatchPerformanceObserver:n}=e;return t&&Object(b.b)(t),n&&n.disconnect(),{isTiming:!1,annotations:[],binaryAnnotations:{},spans:[],traceId:Object(c.a)()}}if("abort"===e.type&&t.isTiming){e.stopwatchPerformanceObserver&&e.stopwatchPerformanceObserver.disconnect();const{metricId:n,pwtStaticContext:a,isAuth:r}=t,i=e.reason||"";return Object(s.a)({metricId:n,pwtStaticContext:a,result:{type:"ABORT",reason:i},isAuth:r}),{isTiming:!1,annotations:[],binaryAnnotations:{},spans:[],traceId:Object(c.a)()}}}return t};e.a=({name:t,sampleRate:e,isAuth:n,navigationType:r,manualAndResourceSpans:i=!1})=>{const s=Object(l.c)(),u=Object(a.useRef)([]),p=Object(a.useRef)(),[d,m]=Object(a.useReducer)(y,{isTiming:!1,annotations:[],binaryAnnotations:{},spans:[],traceId:Object(c.a)()});return s?{isTiming:d.isTiming,start:a=>{if(window.PerformanceObserver){const t=1e3;u.current=[],p.current=Object(o.a)({entryTypes:["resource"]},e=>{u.current=u.current.concat(e.getEntries()),u.current.length>t&&(u.current=u.current.slice(-t))})}const i={type:"start",startTime:a,name:t,navigationType:r,pwtStaticContext:s,isSampled:!e||Math.random()<e,isAuth:n};return m(i)},stop:t=>m({type:"stop",stopTime:t,stopwatchPerformanceObserver:p.current,customStopwatchBuffer:u.current,manualAndResourceSpans:i}),error:t=>{m({type:"error",stopwatchPerformanceObserver:p.current,error:t})},abort:t=>m({type:"abort",stopwatchPerformanceObserver:p.current,customStopwatchBuffer:u.current,reason:t}),annotate:(t,e)=>m({type:"annotate",label:t,parentId:e}),binaryAnnotate:(t,e,n,a)=>m({type:"binaryAnnotate",name:t,value:e,annotationType:n,parentId:a}),binaryAnnotateOperation:(t,e,n,a)=>m({type:"binaryAnnotateOperation",name:t,binaryAnnotationValueAndType:e,operation:n,parentId:a}),addSubspan:(t,e,n,a={},r={},i=null)=>m({type:"addSubspan",name:t,startTime:e,endTime:n,annotations:a,binaryAnnotations:r,parentId:i}),subspanStart:(t,e={},n={},a=null,r=null)=>m({type:"subspanStart",name:t,annotations:e,binaryAnnotations:n,parentId:a,id:r}),subspanStop:(t,e={},n={})=>m({type:"subspanStop",name:t,annotations:e,binaryAnnotations:n}),getSpans:(t,e)=>d.spans.filter(n=>n[t]===e)}:null}},EHyI:function(t,e,n){n.d(e,"a",(function(){return o}));var a=()=>{var t;return!(null===(t=window.performance)||void 0===t||!t.timing)},r=n("XtwW"),i=n("gg0E");function o(t){return!("desktop"===t&&!a())&&(!!r.a&&Object(i.a)())}},LvPn:function(t,e,n){n.d(e,"a",(function(){return c}));var a=n("FylZ"),r=n("pody"),i=n("nEAA");const o=({category:t,isDeferred:e,isExternal:n})=>[t].concat(e?["deferred"]:[]).concat(n?["external"]:[]).join("_");function c(t,e){const{category:n,timing:c,isDeferred:s,isExternal:u,isVisuallyCompleteRequired:p}=t;return c.responseEnd&&("image"!==n||p)?{name:o(t),id:Object(a.a)(),parentId:e,startTime:c.startTime,endTime:c.responseEnd,annotationMap:Object(r.a)(c),binaryAnnotationMap:{category:Object(i.d)(n),decodedBodySize:Object(i.b)(c.decodedBodySize||0),initiatorType:Object(i.d)(c.initiatorType),isDeferred:Object(i.a)(s),isExternal:Object(i.a)(u),name:Object(i.d)(c.name),nextHopProtocol:Object(i.d)(c.nextHopProtocol),transferSize:Object(i.b)(c.transferSize||0)}}:null}},ONNR:function(t,e,n){n.d(e,"a",(function(){return b})),n.d(e,"b",(function(){return j})),n.d(e,"c",(function(){return E})),n.d(e,"d",(function(){return I}));var a,r,i,o,c=function(t,e){return{name:t,value:void 0===e?-1:0,delta:0,entries:[],id:"v1-".concat(Date.now(),"-").concat(Math.floor(8999999999999*Math.random())+1e12)}},s=function(t,e){try{if(PerformanceObserver.supportedEntryTypes.includes(t)){var n=new PerformanceObserver((function(t){return t.getEntries().map(e)}));return n.observe({type:t,buffered:!0}),n}}catch(t){}},u=!1,p=function(t,e){u||"undefined"!=typeof InstallTrigger||(addEventListener("beforeunload",(function(){})),u=!0),addEventListener("visibilitychange",(function n(a){"hidden"===document.visibilityState&&(t(a),e&&removeEventListener("visibilitychange",n,!0))}),!0)},d=function(t){addEventListener("pageshow",(function(e){e.persisted&&t(e)}),!0)},m=new WeakSet,l=function(t,e,n){var a;return function(){e.value>=0&&(n||m.has(e)||"hidden"===document.visibilityState)&&(e.delta=e.value-(a||0),(e.delta||void 0===a)&&(a=e.value,t(e)))}},b=function(t,e){var n,a=c("CLS",0),r=function(t){t.hadRecentInput||(a.value+=t.value,a.entries.push(t),n())},i=s("layout-shift",r);i&&(n=l(t,a,e),p((function(){i.takeRecords().map(r),n()})),d((function(){a=c("CLS",0),n=l(t,a,e)})))},f=-1,y=function(){return"hidden"===document.visibilityState?0:1/0},O=function(){p((function(t){var e=t.timeStamp;f=e}),!0)},v=function(){return f<0&&(f=y(),O(),d((function(){setTimeout((function(){f=y(),O()}),0)}))),{get timeStamp(){return f}}},j=function(t,e){var n,a=v(),r=c("FCP"),i=s("paint",(function(t){"first-contentful-paint"===t.name&&(i&&i.disconnect(),t.startTime<a.timeStamp&&(r.value=t.startTime,r.entries.push(t),m.add(r),n()))}));i&&(n=l(t,r,e),d((function(a){r=c("FCP"),n=l(t,r,e),requestAnimationFrame((function(){requestAnimationFrame((function(){r.value=performance.now()-a.timeStamp,m.add(r),n()}))}))})))},g={passive:!0,capture:!0},w=new Date,T=function(t,e){a||(a=e,r=t,i=new Date,A(removeEventListener),S())},S=function(){if(r>=0&&r<i-w){var t={entryType:"first-input",name:a.type,target:a.target,cancelable:a.cancelable,startTime:a.timeStamp,processingStart:a.timeStamp+r};o.map((function(e){e(t)})),o=[]}},h=function(t){if(t.cancelable){var e=(t.timeStamp>1e12?new Date:performance.now())-t.timeStamp;"pointerdown"==t.type?function(t,e){var n=function(){T(t,e),r()},a=function(){r()},r=function(){removeEventListener("pointerup",n,g),removeEventListener("pointercancel",a,g)};addEventListener("pointerup",n,g),addEventListener("pointercancel",a,g)}(e,t):T(e,t)}},A=function(t){["mousedown","keydown","touchstart","pointerdown"].map((function(e){return t(e,h,g)}))},E=function(t,e){var n,i=v(),u=c("FID"),b=function(t){t.startTime<i.timeStamp&&(u.value=t.processingStart-t.startTime,u.entries.push(t),m.add(u),n())},f=s("first-input",b);n=l(t,u,e),f&&p((function(){f.takeRecords().map(b),f.disconnect()}),!0),f&&d((function(){var i;u=c("FID"),n=l(t,u,e),o=[],r=-1,a=null,A(addEventListener),i=b,o.push(i),S()}))},I=function(t,e){var n,a=v(),r=c("LCP"),i=function(t){var e=t.startTime;e<a.timeStamp&&(r.value=e,r.entries.push(t)),n()},o=s("largest-contentful-paint",i);if(o){n=l(t,r,e);var u=function(){m.has(r)||(o.takeRecords().map(i),o.disconnect(),m.add(r),n())};["keydown","click"].map((function(t){addEventListener(t,u,{once:!0,capture:!0})})),p(u,!0),d((function(a){r=c("LCP"),n=l(t,r,e),requestAnimationFrame((function(){requestAnimationFrame((function(){r.value=performance.now()-a.timeStamp,m.add(r),n()}))}))}))}}},PioT:function(t,e,n){var a=n("+NLT"),r=n("3Qy3");n.d(e,"a",(function(){return r.a}));const i={getBrowser:()=>Object(r.b)(a.a.instance.browser_name||""),isSafari(){return this.getBrowser()===r.a.SAFARI},isChrome(){return this.getBrowser()===r.a.CHROME},isFirefox(){return this.getBrowser()===r.a.FIREFOX}};e.b=i},fZG9:function(t,e,n){n.d(e,"a",(function(){return y})),n.d(e,"b",(function(){return v}));var a=n("bNC6"),r=n("HMdf"),i=n("+lzj"),o=n("SyXB"),c=n("nEAA");const s=(t,e)=>(t||[]).reduce((t,n)=>({...t,["experiment."+n]:Object(c.d)(e(n))}),{}),u=(t,e)=>"number"==typeof e?t(e):null,p=t=>t.reduce((t,e)=>t+e,0),d=(t,e)=>Object.keys(e).reduce((n,a)=>({...n,[`${t}${a}`]:e[a]}),{}),m=t=>{if(!t.length)return{};const e=t.map(({startTime:t,requestStart:e,responseStart:n,responseEnd:a})=>{const r=e||t;return{startTime:t,requestStart:r,responseStart:n||r,responseEnd:a}}),n=p(e.map(t=>t.requestStart-t.startTime)),a=p(e.map(t=>t.responseStart-t.requestStart)),r=p(e.map(t=>t.responseEnd-t.responseStart)),i=n+a+r,o=p(t.map(t=>t.decodedBodySize||0));return{decodedBodySize:Object(c.b)((s=o,Number(Number(s/1024).toFixed(3)))),"duration.all":Object(c.b)(i),"duration.requestStartToResponseStart":Object(c.b)(a),"duration.responseStartToResponseEnd":Object(c.b)(r),"duration.startToRequestStart":Object(c.b)(n)};var s},l=t=>{const e=t.filter(t=>!!t.responseEnd);return{...t.length?{...m(e),"count.completed":Object(c.b)(e.length)}:{},"count.all":Object(c.b)(t.length)}},b=t=>{const e=t.reduce((t,e)=>(t[e.category]=(t[e.category]||[]).concat([e]),t),{}),n={script:e.script,script_deferred:t.filter(t=>t.isDeferred),external:t.filter(t=>t.isExternal),css:e.css,image:e.image,video:e.video,xmlhttprequest:e.xmlhttprequest,visually_complete:t.filter(t=>t.isVisuallyCompleteRequired)};return Object.keys(n).reduce((t,e)=>({...t,...d(`resource.${e}.`,l((n[e]||[]).map(t=>t.timing)))}),{})},f=(t,e)=>{const{devicePixelRatio:n,navigator:r,innerWidth:i,innerHeight:o}=window,{deviceMemory:s,hardwareConcurrency:u,platform:p,userAgent:d}=r,{appType:m,appVersion:l,browserName:b,browserVersion:f,deviceType:y,isBot:O,isSocialBot:v,locale:j,osName:g,stageName:w}=e,T="desktop"===y?m||5:m||6;let S;const{navigationType:h}=t;return S="initial_app_load"===h?1:4,{"app.type":Object(c.c)(T),"app.version":Object(c.d)(l),"browser.name":Object(c.d)(b),"browser.version":Object(c.d)(f),"cpu.speed":Object(c.c)(u),"device.memory":Object(c.c)(s),"device.type":Object(c.c)(0),"device.typeName":Object(c.d)(y),"device.version":Object(c.d)("unknown"),"pwt.cause":Object(c.c)(S),"pwt.result":Object(c.c)(1),"view.type":Object(c.b)(0),"viewport.height":Object(c.b)(o||0),"viewport.width":Object(c.b)(i||0),devicePixelRatio:Object(c.b)(n||0),isBot:Object(c.a)(O),isSocialBot:Object(c.a)(v),locale:Object(c.d)(j),osName:Object(c.d)(g),platform:Object(c.d)(p||null),profilerVersion:Object(c.d)("3"),pwtActionName:Object(c.c)(Object(a.a)(t)),stageName:Object(c.d)(w),userAgent:Object(c.d)(d)}},y=({metricId:t,pwtStaticContext:e,binaryAnnotations:n={},performanceResourceTimings:a=[]})=>{let i={};{const{connection:t,hardwareConcurrency:e,deviceMemory:n}=window.navigator;i={"net.effectiveType":Object(c.d)((null==t?void 0:t.effectiveType)||null),"net.rtt":Object(c.b)(u(t=>10*Math.round(t/10),null==t?void 0:t.rtt)),"net.speed":Object(c.b)(Object(r.b)(a,!1)),"cpu.threads":Object(c.c)(e),"memory.size":Object(c.b)(n)}}return{...f(t,e),...n,...i}},O=(t,e,n,a)=>{var s;const{navigator:d}=window,{connection:m,serviceWorker:l}=d,{surface:b,navigationType:f,isAuthenticated:y}=t,{cumulativeLayoutShiftScore:O,longTaskDurations:v}=Object(i.b)();return{...v.length?{"longTask.count":Object(c.b)(v.length),"longTask.maxDuration":Object(c.b)(Math.max(...v)),"longTask.totalDuration":Object(c.b)(p(v))}:{},cumulativeLayoutShiftScore:Object(c.b)(100*O),"masonry.paginationMarkCount":Object(c.b)(Object(o.e)(o.a,e)),"metricId.isAuthenticated":Object(c.a)(y),"metricId.navigationType":Object(c.d)(f),"metricId.surface":Object(c.d)(b),"net.effectiveType":Object(c.d)((null==m?void 0:m.effectiveType)||null),"net.rtt":Object(c.b)(u(t=>10*Math.round(t/10),null==m?void 0:m.rtt)),"net.speed":Object(c.b)(Object(r.b)(n)),entryChunkAfterDoc:Object(c.a)(a),resourceBufferClearedCount:Object(c.c)(Object(o.e)("resourceBufferCleared",e)),scrollDuringLayout:Object(c.a)(Object(o.f)("scrollDuringLayout",e)),serviceWorker:Object(c.a)(l?!!l.controller:null),serviceWorkerState:Object(c.d)((null==l||null===(s=l.controller)||void 0===s?void 0:s.state)||null)}},v=({annotateExperiments:t,binaryAnnotations:e={},entries:n,entryChunkAfterDoc:a,metricId:r,performanceResources:i,pwtEndTime:o,pwtStaticContext:c})=>({...e,...b(i),...s(t,c.getExperimentGroup),...f(r,c),...O(r,o,n,a)})},mRg4:function(t,e,n){n.d(e,"a",(function(){return v}));let a=null;var r=(t,e)=>(a=a||{results:[],context:e},a.results.push(t),a),i=n("FZ8N"),o=n("LrH5"),c=n("bNC6"),s=n("3/Bf"),u=n("o9su"),p=n("FylZ");const d=(t,e)=>Object.keys(t).reduce((n,a)=>{const r=t[a];return r&&(n[a]={timestamp:e+r}),n},{}),m=({span:t,timeOrigin:e})=>{return{id:t.id,parent_id:t.parentId||null,result:1,name:t.name,timestamp:e+t.startTime,duration:t.endTime-t.startTime,annotations:d(t.annotationMap,e),binary_annotations:(n=t.binaryAnnotationMap,Object.keys(n).reduce((t,e)=>{const a=n[e];if(!a)return t;const{value:r,type:i}=a;return null==r?t:t.concat({name:e,value:r,annotation_type:i})},[]))};var n},l=(t,{startTime:e,endTime:n,annotationMap:a,binaryAnnotationMap:r,parentId:i,traceId:o})=>({name:"pwt/"+t,startTime:e,endTime:n,annotationMap:a,binaryAnnotationMap:r,parentId:i,id:o}),b=({annotations:t})=>t.reduce((t,{key:e,timestamp:n})=>({...t,["server_"+e]:{timestamp:n}}),{}),f=(t,e)=>({...t,annotations:{...b(e),...t.annotations},binary_annotations:[...e.binary_annotations,...t.binary_annotations]}),y=({traceId:t,actionName:e,result:n,timeOrigin:a,serverDataToJoin:r})=>{let i=m({span:l(e,n),timeOrigin:a}),o=null;return r&&(i=f(i,r),o=((t,e,n)=>{const a=Object(u.a)();return(null==a?void 0:a.responseEnd)?f(m({span:{name:"html",startTime:0,endTime:(null==a?void 0:a.responseEnd)||1,annotationMap:{},binaryAnnotationMap:{},id:t.server_span_id||Object(p.a)(),parentId:e},timeOrigin:n}),t):null})(r,t,a)),{trace_id:t,spans:[i,...o?[o]:[],...n.spans.map(t=>m({span:t,timeOrigin:a}))]}},O=Object(o.a)("reportResult");function v({metricId:t,pwtStaticContext:e,result:n,isAuth:a}){const{ajax:o,serverData:u}=e,p=Object(c.b)(t),d=`${n.type}.${p}`,m=void 0!==a&&{tags:{isAuth:a}}||void 0;if(Object(s.c)(n.reason?d.concat("."+n.reason):d,m),"COMPLETE"!==n.type)return void O("Abort metric "+p,n);const l=null!==(b=window.performance)&&void 0!==b&&b.now?Date.now()-window.performance.now():"unknown";var b,f;if("unknown"===l)return O(`Unable to convert to absolute times for ${p} due to missing time origin`),void Object(s.c)("missingTimeOrigin."+p,m);if(i.c&&(window.PWT_LAB_DATA=r(n,e)),n.spans.length&&(n.spans=n.spans.map(t=>(t.parentId||t.id===n.traceId||"network_resources"===t.name||(t.parentId=n.traceId),t))),!i.c){const a=t.navigationType&&"initial_app_load"===t.navigationType,r=n.traceId,c=y({traceId:r,actionName:p,result:n,timeOrigin:l,serverDataToJoin:a&&u||null});o({type:"POST",url:"/_/_/trace/trace/",data:{report_data:JSON.stringify(c),report_context:JSON.stringify((f=e,{debugTrace:i.a,locale:f.locale,stageName:f.stageName,userId:f.isAuthenticated?f.userId:null}))}}),O(`PinTrace ${p} will be available shortly: https://pintrace.pinadmin.com/zipkin/traces/${r}`,{duration:n.endTime-n.startTime,result:n,pwtStaticContext:e})}}},nEAA:function(t,e,n){n.d(e,"c",(function(){return r})),n.d(e,"b",(function(){return i})),n.d(e,"d",(function(){return o})),n.d(e,"a",(function(){return c}));const a=t=>"number"==typeof t?Math.round(t):t,r=t=>({type:"I16",value:a(t)}),i=t=>({type:"I32",value:a(t)}),o=t=>({type:"STRING",value:t}),c=t=>({type:"BOOL",value:t})},o9su:function(t,e,n){var a=n("XtwW");e.a=()=>{const[t]=a.a?a.a.getEntriesByType("navigation"):[];return t}},pody:function(t,e,n){e.a=t=>({connectEnd:t.connectEnd||0,connectStart:t.connectStart||0,domainLookupEnd:t.domainLookupEnd||0,domainLookupStart:t.domainLookupStart||0,fetchStart:t.fetchStart||0,requestStart:t.requestStart||0,redirectEnd:t.redirectEnd||0,redirectStart:t.redirectStart||0,responseEnd:t.responseEnd||0,responseStart:t.responseStart||0,secureConnectionStart:t.secureConnectionStart||0,startTime:t.startTime||0,workerStart:t.workerStart||0})},xfna:function(t,e,n){n.d(e,"a",(function(){return l})),n.d(e,"b",(function(){return b})),n.d(e,"c",(function(){return f}));var a=n("q1tI"),r=n("EHyI"),i=n("gg0E"),o=n("SyXB"),c=n("3/Bf"),s=n("+lzj"),u=n("HMdf"),p=n("nKUr");const d=Object(a.createContext)(null),m=Object(a.createContext)(null);function l({children:t,immutableLocation:e,resourceTimingCacheSize:n,routerHistoryAction:l,staticContext:b}){const f=Object(a.useRef)(null),y=Object(a.useRef)(null),O=Object(a.useRef)(e),v=Object(a.useRef)(!0);if(Object(a.useEffect)(()=>{Object(u.e)({size:n||1e3}),Object(s.c)(b),Object(c.c)("totalSessionVolume"),window.performance?["clearMarks","clearMeasures","clearResourceTimings","getEntries","getEntriesByName","getEntriesByType","mark","measure","now","setResourceTimingBufferSize"].forEach(t=>{window.performance[t]||Object(c.c)("not_supported.window.performance."+t)}):Object(c.c)("not_supported.window.performance"),window.PerformanceObserver||Object(c.c)("not_supported.window.PerformanceObserer"),Object(i.a)()||Object(c.c)("not_supported.grid_profiler"),v.current=!1},[]),O.current!==e){O.current=e,y.current=null!==(j=window.performance)&&void 0!==j&&j.now?window.performance.now():null;const{current:t}=y;if(!v.current){Object(c.c)("routeStart",{tags:{action:l}}),Object(u.a)(),Object(s.a)(),Object(o.b)();const{customBufferSize:e,defaultBufferSize:n}=Object(u.d)();t&&(Object(c.c)("routeStart.customBufferSize",{count:e}),Object(c.c)("routeStart.defaultBufferSize",{count:n}),f.current={time:t,action:l})}}var j;return Object(p.jsx)(d.Provider,{value:Object(r.a)(b.deviceType)?b:null,children:Object(p.jsx)(m.Provider,{value:f.current,children:t})})}const b=()=>Object(a.useContext)(m),f=()=>Object(a.useContext)(d)}}]);
//# sourceMappingURL=https://sm.pinimg.com/webapp/57-f431d9a2c461409475a9.mjs.map