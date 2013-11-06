$(function () {
    function updateElementIndex(el, prefix, ndx) {
        var id_regex = new RegExp('(' + prefix + '-\\d+-)');
        var replacement = prefix + '-' + ndx + '-';

        if ($(el).attr("for")) {
          $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));
        }

        if (el.id) {
          el.id = el.id.replace(id_regex, replacement);
        }

        if (el.name) {
          el.name = el.name.replace(id_regex, replacement);
        }
    }


    function deleteForm(btn, prefix) {
        var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
        if (formCount > 1) {
            $(btn).parents('.item').slideDown(300).remove();
            var forms = $('.item');
            $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
            var i = 0;

            for (formCount = forms.length; i < formCount; i++) {
                $(forms.get(i)).children().children().each(function() {
                    if ($(this).attr('type') == 'text') updateElementIndex(this, prefix, i);
                });
            }
        } else {
            alert("You have to enter at least one member!");
        }
        return false;
    }


    function addForm(btn, prefix) {
        var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
        if (formCount < 10) {
            var row = $(".item:first").clone(false).get(0);
            $(row).removeAttr('id').hide().insertAfter(".item:last").slideDown(300);
            $(".errorlist", row).remove();
            $(row).children().removeClass("error");

            $(row).children().children().each(function () {
                updateElementIndex(this, prefix, formCount);
                $(this).val("");
            });

            $(row).find(".delete").click(function () {
                return deleteForm(this, prefix);
            });

            $("#id_" + prefix + "-TOTAL_FORMS").val(formCount + 1);
        } else {
            alert("Sorry, you can only enter a maximum of ten items.");
        }
        return false;
    }


    $("#add").click(function () {
      if ($('form').hasClass('add')) {
        return addForm(this, 'form');
      } else {
        return addForm(this, 'choice_set')
      }
    });


    $(".delete").click(function () {
      if ($('form').hasClass('delete')) {
        return addForm(this, 'form');
      } else {
        return addForm(this, 'choice_set')
      }
    });


    if ($('form').hasClass('update')) {
      $('.delete').remove();
    }
});