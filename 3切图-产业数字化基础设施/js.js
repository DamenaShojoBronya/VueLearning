window.onload = function() {
    // 进入就加载方法
    tabClick(); //切换方法
}

function tabClick() {
    var tab = document.querySelectorAll(".content-2-list li"); // 获取tab所有 li
    var cont = document.querySelectorAll(".content li") //获取content所有 li
    var img = document.querySelectorAll(".content-2-home li") //获取content所有 li
    
    if (tab && cont && img) { //严格模式 取到tab 和 cont 之后再进行其他
        for (var i = 0; i < tab.length; i++) { //给每一个tab添加点监听点击事件
            addHover(i);
        }
        //添加点击监听
        function addHover(i) {
            tab[i].addEventListener('mouseover', function() { //悬浮切换
                setImgClass(i);
                setContClass(i)
            });
        }
        // // 切换按钮的事件
        // function setTabClass(num) {
        //     // 移出所有的TabActive名称
        //     for (var i = 0; i < tab.length; i++) {
        //         tab[i].classList.remove("TabActive");
        //     }
        //     // 点击的哪个给哪个添加TabActive
        //     tab[num].classList.add("TabActive");
        // }
        
        // 切换内容的事件
        function setContClass(num) {
            // 移出所有的ContActive名称
            for (var i = 0; i < cont.length; i++) {
                cont[i].classList.remove("ContActive");
            }
            // 点击的哪个给哪个添加ContActive
            cont[num].classList.add("ContActive");
        }
        function setImgClass(num) {
            // 移出所有的ContActive名称
            for (var i = 0; i < img.length; i++) {
                img[i].classList.remove("tabactive");
            }
            // 点击的哪个给哪个添加ContActive
            img[num].classList.add("tabactive");
        }
    }
}