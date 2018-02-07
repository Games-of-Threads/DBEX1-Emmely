import store

store = store.STORE("fruits")
print('In-memory')
store.print_in_mem()
store.tell_me_about_the_store()
store.put_val( 'ananas' ,  '111' )

store.put_val( 'mango' ,  [1,2,3,] )
store.put_val( 'banana' ,  {'333':333} )

store.put_val( 'apple' ,  '222' )
store.put_val( 'pear' ,  '333' )
print(store.read_val('pear'))
print('In-memory')
store.print_in_mem()

store.read_val( 'apple7' )
print(store.get_all())
store.delete_val('pear')
print (store.get_all())
print (store.get_all_by_type())
