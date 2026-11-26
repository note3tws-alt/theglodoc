(function(){
  var S=window.SITE||{};
  document.querySelectorAll("[data-site]").forEach(function(el){var v=S[el.getAttribute("data-site")];if(v)el.textContent=v;});
  document.querySelectorAll("[data-site-href]").forEach(function(el){var v=S[el.getAttribute("data-site-href")];if(v)el.href=v;});
  document.querySelectorAll("[data-site-mailto]").forEach(function(el){var v=S[el.getAttribute("data-site-mailto")];if(v)el.href="mailto:"+v;});
  /* count-up for the consultations figure, runs once when it scrolls into view */
  var big=document.querySelector(".bignum");
  if(big&&!matchMedia("(prefers-reduced-motion: reduce)").matches&&"IntersectionObserver" in window){
    var full=big.textContent.trim(),target=parseInt(full.replace(/[^0-9]/g,""),10),suffix=full.replace(/^[0-9,]+/,"");
    if(target>1){
      var io=new IntersectionObserver(function(es){
        if(!es[0].isIntersecting)return;io.disconnect();
        var t0=null,dur=1400;
        function step(t){
          if(t0===null)t0=t;var k=Math.min(1,(t-t0)/dur),e=1-Math.pow(1-k,3);
          var n=Math.max(1,Math.round(1+(target-1)*e));
          big.textContent=n.toLocaleString("en-US")+(k===1?suffix:"");
          if(k<1)requestAnimationFrame(step);else big.textContent=full;
        }
        big.textContent="1";requestAnimationFrame(step);
      },{threshold:.4});
      io.observe(big);
    }
  }
  var c=0;
  document.querySelectorAll(".reveal .w i").forEach(function(w){
    var inName=!!w.closest(".nm"),t=w.textContent;w.textContent="";
    t.split("").forEach(function(ch){var s=document.createElement("span");s.className="l";if(inName)s.style.setProperty("--c",c++);s.textContent=ch;w.appendChild(s);});
  });
})();

(function(){
  document.querySelectorAll("form.enq-form").forEach(function(form){
    var btn=form.querySelector("button[type=submit]"),st=form.querySelector(".enq-status"),label=btn.textContent;
    form.addEventListener("submit",function(e){
      e.preventDefault();
      st.className="enq-status";
      if(!window.GLODOC_LIVE){st.textContent="Preview only. Enquiries are sent from the live website.";return;}
      btn.disabled=true;btn.textContent="Sending...";st.textContent="";
      fetch("/",{method:"POST",headers:{"Content-Type":"application/x-www-form-urlencoded"},body:new URLSearchParams(new FormData(form)).toString()})
      .then(function(r){if(!r.ok)throw new Error(r.status);form.reset();st.textContent="Thank you. Your message has been sent and the team will be in touch.";})
      .catch(function(){st.className="enq-status err";st.textContent="Your message didn't send. Please try again, or message "+((window.SITE&&SITE.instagramHandle)||"@the.glodoc")+" on Instagram.";})
      .then(function(){btn.disabled=false;btn.textContent=label;});
    });
  });
})();
