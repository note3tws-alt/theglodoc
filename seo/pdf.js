// Renders the printable media kit to PDF. Usage: node seo/pdf.js <in.html> <out.pdf>
const {chromium}=require('playwright');const path=require('path');
(async()=>{const [inp,out]=process.argv.slice(2);const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+path.resolve(inp),{waitUntil:'load'});
await p.pdf({path:out,format:'A4',printBackground:true,preferCSSPageSize:true});await b.close();console.log('wrote',out);})();
