window.onload = function () {
    const {createEditor, createToolbar} = window.wangEditor;

    const editorConfig = {
        placeholder: 'Type here...',
        onChange(editor) {
            const html = editor.getHtml();
            console.log('editor content changed:', html); // 调试信息
        },
    };

    const editor = createEditor({
        selector: '#editor-container',
        html: '<p><br></p>',
        config: editorConfig,
        mode: 'default', // or 'simple'
    });

    const toolbarConfig = {};

    const toolbar = createToolbar({
        editor,
        selector: '#toolbar-container',
        config: toolbarConfig,
        mode: 'default', // or 'simple'
    });

    $('#submit-btn').click(function (event) { // 确保使用 jQuery 选择器
        event.preventDefault();

        let title = $("input[name='title']").val();
        let category = $("#category-select").val();

        let content = editor.getHtml();

        if (!content || content.trim() === '<p><br></p>') {
            alert("请在编辑器中输入内容");
            return;
        }

        let csrfmiddlewaretoken = $("input[name='csrfmiddlewaretoken']").val();

        $.ajax('/blog/pub', {
            method: 'post',
            data: {title, content, category, csrfmiddlewaretoken},
            success: function (res) {
                if (res['code'] === 200) {
                    let blog_id = res['data']['blog_id'];
                    window.location.href = '/blog/' + blog_id;

                } else {
                    alert(res['msg']);
                }
            },
            error: function (xhr, status, error) {
                console.error('AJAX 请求失败:', xhr.responseText);
                alert("发布失败，请稍后再试");
            },
        });
    });
}