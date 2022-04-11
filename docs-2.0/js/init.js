(function(){
    $("img").click(function change(){
        var $this = $(this)
        $(this).toggleClass("max");
        $("#dialog-bg").toggleClass("dialog-bg");
    });
    $("#dialog-bg").on("click",function () {
        $("#dialog-bg").toggleClass("dialog-bg");
        $("img").each(function(){
            if($(this).hasClass("max")){
                $(this).toggleClass("max");
            }
        })
    });
})()