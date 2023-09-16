def main_menu_display():
    print()
    print('=============  Data Karyawan Divisi Data Science  =============')
    print()
    print('1. List Daftar Karyawan')
    print('2. Menambahkan Data Karyawan Baru')
    print('3. Mengubah Data Karyawan')
    print('4. Menghapus Data Karyawan')
    print('5. Exit')
    print()
    print('Silahkan pilih menu yang ingin di akses(1 - 5):', end=' ')
    user_input=int(input())
    print()
    main_menu(user_input)

def main_menu(i:int):
    '''
    Memilih menu yang diinginkan
    '''
    if i == 1:
        database_menu_display()
    elif i == 2:
        pass
    elif i == 3:
        pass
    elif i == 4:
        pass
    elif i == 5:
        print('Terima kasih telah mengakses daftar karyawan')
        print('-----------  Have a good day  --------------')
        print()
        quit()
    else:
        print('Pilihan menu yang dipilih tidak tersedia')
        print('Mohon pilih ulang menu yang yang tersedia')
        main_menu_display()

def database_menu_display():
    print('=============  Database Karyawan  =============')
    print()
    print('1. Tampilkan data seluruh karyawan')
    print('2. Tampilkan data karyawan')
    print('3. Kembali ke menu utama')
    print()
    print('Silahkan pilih menu yang ingin di akses (1-3):', end=' ')
    user_input = int(input())
    database_menu(user_input)

def database_menu(i:int):
    '''
    Memilih menu yang diinginkan
    '''
    if i == 1:
        show_database()
    elif i == 2:
        show_employee()
    elif i == 3:
        print('Kembali ke Menu Utama')
        print()
        main_menu_display()
    else:
        print()
        print('Pilihan menu tidak tersedia')
        print('Mohon pilih ulang menu yang yang tersedia')
        print()
        database_menu_display()

def show_database():
    print()
    for employee_name, employee_data in employee_database.items():
        print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(employee_name, 
                                               employee_data['ID'],
                                               employee_data['Tempat Lahir'],                                                   employee_data['Tanggal Lahir'],
                                               employee_data['Alamat'],
                                               employee_data['Golongan Darah'],
                                               employee_data['Agama'],
                                               employee_data['Status Perkawinan']
                                               ))
    print()
    database_menu_display()

def show_employee():
    print()
    print('Masukkan nama lengkap karyawan:', end=' ')
    name_input = input().lower()
    name_input = name_input.title()
    print()

    for employee_name, employee_data in employee_database.items():
        if name_input == employee_name:
            print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(employee_name,
                                                        employee_data['ID'],
                                                        employee_data['Tempat Lahir'],                                                   employee_data['Tanggal Lahir'],
                                                        employee_data['Alamat'],
                                                        employee_data['Golongan Darah'],
                                                        employee_data['Agama'],
                                                        employee_data['Status Perkawinan']
                                                        ))
            print()
            break
        else:
            print('Data karyawan tidak ditemukan!')
            print('Masukkan ulang nama karyawan')
            print()
            show_employee()
    
    print('Apakah anda ingin mengedit data karyawan?')
    print('1. Ya')
    print('2. Tidak')
    print('Input (1-2):', end = ' ')
    user_input=int(input())
    
    # edit_database = True
    while True:
        if user_input == 1:
            pass
        elif user_input == 2:
            print()
            print('Kembali ke Menu Database')
            print()
            database_menu_display()
        else:
            print('Perintah tidak ditemukan!')
            print('Mohon pilih ulang (1-2):', end = ' ')
            user_input=int(input())

# def add_employee_data():

employee_database={
    'Viky':{
        'ID' : 'DS150798',
        'Tempat Lahir' : 'Surabaya',
        'Tanggal Lahir' : '15 Juli 1998',
        'Alamat' : 'Gayungsari Barat 2 no. 23',
        'Golongan Darah' : 'A',
        'Agama' : 'Islam',
        'Status Perkawinan' : 'Belum Kawin'
        },
    'Aldo':{
        'ID' : 'DS081097',
        'Tempat Lahir' : 'Surabaya',
        'Tanggal Lahir' : '8 Oktober 1997',
        'Alamat' : 'Kebonagung Blok 2A no. 14',
        'Golongan Darah' : 'B',
        'Agama' : 'Islam',
        'Status Perkawinan' : 'Belum Kawin'
        }
}

main_menu_display()