import os.path
import pickle


# Defining the class
class STORE:
    
    def __init__(self, dbname):
        self.dbname = "./" + dbname + "/" +dbname
        if not os.path.exists(dbname):
            os.makedirs(dbname)
        self.memory = {}
        #If database exist the open the database
        if ( os.path.isfile( self.dbname ) ):
            self.memory = pickle.load( open( self.dbname, "rb" ) )
        else:
            #Else create ir
            pickle.dump( self.memory, open( self.dbname , "wb" ) )

    def tell_me_about_the_store(self):
        print("This key value store has the name <" + self.dbname + ">.")
        print("The in-memory dictonary is persisted in a file named <" + self.dbname + ">.")
        print("This key value store is persisted on disk in up to ten files named <" + self.dbname + "_[0-9]_store > .")

    def put_val(self, key, value):
        suffix = str(hash( key ))[-1]
        disk_file = self.dbname + "_" + suffix +"_store"  
        self.memory[key] = None #just want the key in in-memory dictonary
        store = {}
        if ( os.path.isfile( disk_file ) ):
            store = pickle.load( open( disk_file , "rb" ) )
            #Loading The existing store
        store[key] = value # type independent
        pickle.dump( store, open( disk_file , "wb" ) )
        ## only keys persisted
        z = {}
        for k in self.memory:
            z[k] = None
        pickle.dump( z, open( self.dbname , "wb" ) )
        
    def read_val(self, key):
        suffix = str(hash( key ))[-1]
        disk_file = self.dbname + "_" + suffix +"_store"  
        if key in self.memory:
            if( self.memory[key] != None ):
                return self.memory[key]
            else:            
                store = {}
                if ( os.path.isfile( disk_file) ):
                    store = pickle.load( open( disk_file , "rb" ) )
                    if key in store :
                        self.memory[key] = store[key]
                        return store[key]
                    else:
                        print('Key does not exist')
                        return None
        else:
            print('Varning: No key in memory');
            return None
    def delete_val(self, key):
        suffix = str(hash( key ))[-1]
        disk_file = self.dbname + "_" + suffix +"_store"  
        if key in self.memory:
            del self.memory[key]           
        store = {}
        if ( os.path.isfile( disk_file) ):           
            store = pickle.load( open( disk_file , "rb" ) )
            if key in store:
                del store[key]
                pickle.dump( store, open( disk_file , "wb" ) )

        else:
            print('key not found. Nothing was deleted')
   
    def get_all(self):
        z = {}
        for suffix in range(10):
            disk_file = self.dbname + "_" + str(suffix) +"_store"             
            if ( os.path.isfile( disk_file) ):
                store = pickle.load( open( disk_file , "rb" ) )
                if( len( store ) > 0 ):
                    z.update( store )
        return z
    def get_all_by_type(self):
        z = {}
        for suffix in range(10):
            disk_file = self.dbname + "_" + str(suffix) +"_store"             
            if ( os.path.isfile( disk_file) ):
                store = pickle.load( open( disk_file , "rb" ) )
                if( len( store ) > 0 ):
                    for k in store:
                        z[k] = type(store[k])
        return z
    def print_in_mem(self):
        print(self.memory)