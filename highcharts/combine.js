const obj1 = JSON.parse(json1);
const obj2 = JSON.parse(json2);


const mergedObj = Object.assign(obj1, obj2);

const jsonStr = JSON.stringify(mergedObj);