var a = prompt("請輸入數字", "0");
        if (a < 0) {
            document.write("您輸入的值是*負數*");
        }
        else if(a % 2 != 0) {
            document.write("您輸入的值是奇數");
        }
        else{
            document.write("您輸入的值是偶數");
        }