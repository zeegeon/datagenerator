// const http = require("http");
// const app = http.createServer((request, response) => {
//   const _url = request.url;
//   const fullUrl = new URL("http://localhost:7777" + _url);
//   const pathName = fullUrl.pathname;

//   if (pathName === "/") {
//     response.writeHead(200, { "Content-Type": "text/html;charset= utf-8" });
//     response.end(`<h1>Test server test</<h1>`);
//   }

//   if (pathName === "/make") {
//     response.writeHead(200, { "Content-Type": "text/html;charset= utf-8" });
//     response.end(`<h1>make mock data </<h1>`);
//   }
// });

// app.listen(7777, () => {
//   //포트번호 7777으로 서버 구동
//   console.log("서버 시작 주소: http:localhost:7777");
// });

// 아래는 open API 서버 구동 코드
const { Configuration, OpenAIApi } = require("openai");

const configiration = new Configuration({});

const openai = new OpenAIApi(configiration);

const runPrompt = async () => {
  const response = await openai.createCompletion({
    model: "text-davinci-003",
    prompt:
      "한국인 20대 여성에 대한 하루 소비내역 데이터를 json형식으로 더미 파일 예시를 2개 만들어줘",
    max_tokens: 300,
    temperature: 0.2,
  });
  console.log(response.data.choices[0].text);
  //console.log("- completion:\n" + response.data.choices[0].text);
  //console.log("\n- total tokens: " + response.data.usage.total_tokens);
};
runPrompt();

// DB 삽입

// 웹 환경에서 호출
// async function callChatGPTAPI(prompt) {
//   const url = "https://api.openai.com/v1/engines/davinci-codex/completions";
//   const headers = {
//     "Content-Type": "application/json",
//     Authorization: "Bearer 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",
//   };
//   const data = {
//     prompt: prompt,
//     max_tokens: 50,
//   };

//   try {
//     const response = await fetch(url, {
//       method: "POST",
//       headers: headers,
//       body: JSON.stringify(data),
//     });
//     const responseData = await response.json();
//     return responseData.choices[0].text;
//   } catch (error) {
//     console.error("API call error:", error);
//     return null;
//   }
// }

// const prompt =
//   "한국인 20대 여성에 대한 소비내역 데이터를  json형식으로 더미 파일 예시를 2개 만들어줘";
// callChatGPTAPI(prompt)
//   .then((response) => console.log(response))
//   .catch((error) => console.error("Error:", error));
