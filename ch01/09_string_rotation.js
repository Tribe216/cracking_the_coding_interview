function isStringRotation(str1, str2) {
    if (str1.length !== str2.length) return false;

    const doubledString = str1 + str1;
    return doubledString.includes(str2);
}

const test1 = "bartmach";
const test2 = "achbartm";

console.log(isStringRotation(test1, test2));
