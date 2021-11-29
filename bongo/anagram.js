const value1 = "eat";
const value2 = "bleat";

var sortAlphabets = function(text) {
    return text.split('').sort().join('');
};

const checkAnagram = (v1,v2) => {
    if(v1.length != v2.length){
        return "Values are not anagram";
    }else{
        v1Result = sortAlphabets(v1);
        v2Result = sortAlphabets(v2);

        if(v1Result == v2Result){
            return "Values are anagram";
        }else{
            return "Values are not anagram";
        }

    }
}

console.log("Result : ",checkAnagram(value1,value2))
