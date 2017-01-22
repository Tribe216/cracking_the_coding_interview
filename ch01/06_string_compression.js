function compressString(str) {
  let currentChar = str[0];
  let currentCount = 1;
  let result = "";

  for (let i=1; i <= str.length; i++) {
    const ch = str[i];
    if (ch === currentChar) {
      currentCount++;
    } else {
      result += currentChar + currentCount;
      currentCount = 1;
      currentChar = ch;

      if (result.length >= str.length) {
        result = str;
        break;
      }
    }
  }

  return result;
}

console.log(compressString("aabcccccaaa"));
