// Editorial starter exercises selected only from declared constraints.
const tasks={
 data_analyst:['খরচের হিসাব নিয়ে তিনটি প্রশ্ন লেখো।','নিজের তৈরি ১০টি খরচের সারি ও তারিখ গোছাও।','যোগফল করো এবং একই তথ্য দুইবার আছে কি না দেখো।','কোন খাতে বেশি খরচ তা তুলনা করে একটি সিদ্ধান্ত লেখো।','তিনটি ফলাফল, একটি সীমাবদ্ধতা ও পরের প্রশ্ন লেখো।'],
 digital_marketer:['একটি কাল্পনিক স্থানীয় ব্যবসা ও তার গ্রাহকের সমস্যা লেখো।','গ্রাহক সার্চে করতে পারে এমন পাঁচটি প্রশ্ন লেখো।','প্রশ্নগুলো তথ্য জানা, তুলনা ও সেবা নেওয়ার উদ্দেশ্যে ভাগ করো।','একটি প্রশ্নের উত্তর দিতে একটি পেজের শিরোনাম ও তিনটি পয়েন্ট লেখো।','প্রতিটি প্রশ্নের সঙ্গে উত্তর মেলে কি না যাচাই করে তিন লাইনে ব্যাখ্যা করো।'],
 graphic_designer:['একটি কাল্পনিক অনুষ্ঠানের দর্শক, বার্তা ও দরকারি তথ্য লেখো।','একই বার্তার দুটি layout কাগজে বা নিজের নোটে আঁকো।','শিরোনাম ও মূল তথ্যের আকার আলাদা করে একটি খসড়া বানাও।','ছোট আকারে লেখা পড়া যায় কি না এবং তথ্য ঠিক কি না দেখো।','দুটি layout তুলনা করে কোনটি কেন বেছে নিলে তা লেখো।']
};
export function makeStarterPlan({career,device,minutes}){
 if(!Object.hasOwn(tasks,career)||!['phone','computer'].includes(device)||![15,30,60].includes(minutes))return null;
 const learn=Math.floor(minutes/4),reflect=Math.max(2,Math.floor(minutes/6));
 return {career,device,minutes,blocks:{learn,practice:minutes-learn-reflect,reflect},steps:[...tasks[career]],
  deviceNote:device==='phone'?'ফোনে নোট, কাগজ ও ছোট খসড়া দিয়ে শুরু করো। বড় spreadsheet বা পেশাগত ফাইল তৈরিতে পরে কম্পিউটার লাগতে পারে।':'কম্পিউটারে নিজের তৈরি ডেটা বা খসড়া ব্যবহার করো; প্রথমে নতুন সফটওয়্যার কেনা বা বিজ্ঞাপন চালানো লাগবে না।',
  kind:'editorial-starter-plan',completionGuarantee:false};
}
