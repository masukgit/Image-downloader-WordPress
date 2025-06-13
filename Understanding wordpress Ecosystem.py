def wp_paragraph(text):
    return f'<!-- wp:paragraph --> <p>{text}</p> <!-- /wp:paragraph -->'
my_text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'
my_text2 = 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC.'
print(wp_paragraph(my_text) + (wp_paragraph(my_text2)))

def heading(text3):
    return f'<!-- wp:heading --> <h2 class="wp-block-heading"> {text3} </h2> <!-- /wp:heading -->'
text3 = 'I love Python'
print(heading(text3))

items = ['banana', 'kola', 'dola', 'lala']
my_content = ['<ul>']
for item in items:
    single_list = f'<li>{item}</li>'
    my_content.append(single_list)
my_content.append('</ul>')
my_str = ' '.join(my_content)
final_output = f'<!-- wp:list -->{my_str} <!-- /wp:list -->'

print(final_output)

items = ['banana', 'kola', 'dola', 'lala']
def wp_create_list(items):
    """
    This will convert python list to WordPress html list
    :param items: Any list
    :return: WordPress html list
    """
    my_content = ['<ul>']
    for item in items:
        single_list = f'<li>{item}</li>'
        my_content.append(single_list)
    my_content.append('</ul>')
    my_str = ' '.join(my_content)
    final_output = f'<!-- wp:list -->{my_str} <!-- /wp:list -->'
    return final_output

my_new_list = ['Dal', 'Chal', 'Khesari', 'Chola', 'Mugh', 'Sorisha']

print(wp_create_list(my_new_list))

def wp_h4(text):
    return f'<!-- wp:heading {"level":4} --><h4 class="wp-block-heading">{text}</h4><!-- /wp:heading -->'

text = 'Hamid Mia'
print(wp_h4(text))


