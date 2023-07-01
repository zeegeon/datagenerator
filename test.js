// Open API key
//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

const http = require("http");
const app = http.createServer((request, response) => {
  const _url = request.url;
  const fullUrl = new URL("http://localhost:7777" + _url);
  const pathName = fullUrl.pathname;

  if (pathName === "/") {
    response.writeHead(200, { "Content-Type": "text/html;charset= utf-8" });
    response.end(`<h1>Test server test</<h1>`);
  }

  if (pathName === "/make") {
    response.writeHead(200, { "Content-Type": "text/html;charset= utf-8" });
    response.end(`<h1>make mock data </<h1>`);
  }
});

app.listen(7777, () => {
  //포트번호 7777으로 서버 구동
  console.log("서버 시작 주소: http:localhost:7777");
});
