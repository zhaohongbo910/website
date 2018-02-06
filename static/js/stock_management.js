(function(){
    layui.use(['form', 'layedit', 'laydate'], function() {
        var form = layui.form,
            layer = layui.layer,
            layedit = layui.layedit,
            laydate = layui.laydate;
        laydate.render({
            elem: '#date1'
        });  
        laydate.render({
            elem: '#date2'
        }); 
        laydate.render({
            elem: '#date3'
        });  
        laydate.render({
            elem: '#date4'
        }); 
        laydate.render({
            elem: '#date5'
        });                 
    });
}())