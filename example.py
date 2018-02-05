import store
store = store.STORE("fruits2")


store.tell_me_about_the_store()
store.put_val( 'ananas' ,  '111' )
store.put_val( 'apple' ,  '222' )
store.put_val( 'pear' ,  '333' )
print(store.read_val( 'pear' ))
store.delete_val('pear')
print(store.get_all())
