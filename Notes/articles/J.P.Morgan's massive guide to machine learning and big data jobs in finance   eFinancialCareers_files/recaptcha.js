(function(){var k=function(a){if(a.get&&a.set){var b=a.get("name");a.get("trackingId");window[window.GoogleAnalyticsObject||"ga"]=e(a);g(a,b+"_R_");h()(b+".require",b+"_R_")}},l=function(a){a.get("name")},h=function(){var a=window.GoogleAnalyticsObject||"ga";window[a]=window[a]||function(){(window[a].q=window[a].q||[]).push(arguments)};return window[a]},e=function(a){var b=h(),c=1;return function(){var d=a.get("name");if(1>arguments.length||arguments[0].toLowerCase()!==d+".send"&&"send"!==arguments[0].toLowerCase()||
a.get("&retime")>(new Date).getTime()-18E5||a.get("ex_rec"))return b.apply(window,arguments);var f=d+"_R_"+c;c++;g(a,f);b(d+".require",f);return b.apply(window,arguments)}},g=function(a,b){var c=h();a.set("ex_rec",!0);m(a,function(d){a.set("&retoken",d);a.set("&retime",(new Date).getTime());a.set("ex_rec",!1);c("provide",b,l)})},m=function(a,b){var c=document.getElementById("__ga_rcDiv");c&&c.parentNode.removeChild(c);c=document.createElement("div");var d={id:"__ga_rcDiv",width:0,height:0,display:"none",
visibility:"hidden"},f;for(f in d)d.hasOwnProperty(f)&&c.setAttribute(f,d[f]);document.body.appendChild(c);c=a.get("trackingId")+","+a.get("clientId");b=grecaptcha.render("__ga_rcDiv",{sitekey:"6Lezo0kUAAAAAKhUQ96uCv8HFPUiiB5BkeLRg4wq",size:"invisible",callback:b,"content-binding":c,isolated:!0,badge:"none"});a.get("name");grecaptcha.execute(b)},n=function(){h()("provide","recaptcha",k)},p=["__ga_onLoadReCaptcha__"],q=this;p[0]in q||"undefined"==typeof q.execScript||q.execScript("var "+p[0]);
for(var r;p.length&&(r=p.shift());)p.length||void 0===n?q=q[r]&&q[r]!==Object.prototype[r]?q[r]:q[r]={}:q[r]=n;window.gaplugins=window.gaplugins||{};window.gaplugins.Recaptcha=k;var t=document.createElement("script");t.type="text/javascript";t.async=!0;t.src="https://www.google.com/recaptcha/api.js?onload=__ga_onLoadReCaptcha__&render=explicit";var u=document.getElementsByTagName("script")[0];u.parentNode.insertBefore(t,u);}).call(this);
