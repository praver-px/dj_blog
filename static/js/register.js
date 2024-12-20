$(function () {
    console.log("Document ready"); // 确保文档就绪函数被调用

    function bindCaptchaBtnClick() {
        console.log("bindCaptchaBtnClick called"); // 确保函数被调用
        $("#captcha-btn").click(function (event) {
            console.log("Button clicked"); // 确保按钮点击事件被触发
            let $this = $(this);
            let email = $("input[name='email']").val();
            if (!email) {
                alert("请输入邮箱");
                return;
            }

            // 取消按钮的点击事件
            $this.off('click');

            // 发送请求
            $.ajax('/auth/captcha?email=' + email, {
                method: 'get',
                success: function (res) {
                    if (res['code'] === 200) {
                        alert("验证码已发送，请注意查收");
                    } else {
                        alert(res['msg']);
                    }
                },
                fail: function (error) {
                    console.log(error)
                }
            })

            // 倒计时
            let countdown = 60;
            let timer = setInterval(function () {
                if (countdown <= 0) {
                    $this.text("获取验证码");
                    clearInterval(timer);
                    bindCaptchaBtnClick();
                } else {
                    countdown--;
                    $this.text(countdown + "s");
                }
            }, 1000);
        });
    }

    bindCaptchaBtnClick();
});