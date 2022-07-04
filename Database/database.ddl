create schema schedule_system;
use
schedule_system;

create table admin_users
(
    email        varchar(100) primary key,
    password     varchar(32) not null,
    full_name    varchar(25) not null,
    phone_number varchar(20) not null
);

create table staff_members
(
    email        varchar(100) primary key,
    nhs_number   integer     not null,
    password     varchar(32) not null,
    full_name    varchar(25) not null,
    phone_number varchar(20) not null
);

create table patients
(
    nhs_number   integer primary key,
    full_name    varchar(25)  not null,
    email        varchar(100) not null,
    phone_number varchar(20),
    age          integer      not null
);

create table medications
(
    medication_name     varchar(150) primary key,
    unit_of_measurement varchar(50)   not null,
    amount              decimal(7, 2) not null
);

create table blood_tests
(
    blood_test_type      varchar(100) primary key,
    hours_before_results integer not null
);

create table medications_blood_tests
(
    medication     varchar(150) references medications (medication_name) on update cascade on delete cascade,
    blood_test     varchar(100) references blood_tests (blood_test_type) on update cascade on delete cascade,
    frequency_days integer not null,
    mandatory      boolean not null,
    constraint primary key (medication, blood_test)
);

create table patients_blood_tests
(
    patient_nhs_number integer references patients (nhs_number),
    blood_test         varchar(100) references blood_tests (blood_test_type) on update cascade on delete cascade,
    date_taken         datetime not null,
    constraint primary key (patient_nhs_number, blood_test)
);

create table patients_prescriptions
(
    id                 int primary key,
    patient_nhs_number integer references patients (nhs_number) on update cascade on delete cascade,
    medication_name    varchar(150) references medications (medication_name) on update cascade on delete cascade,
    first_dose         datetime not null,
    days_frequency     integer  not null,
    repetitions        integer  not null,
    end_date           datetime not null
);

create table general_practices
(
    id           integer primary key auto_increment,
    name         varchar(100),
    address      varchar(100) not null,
    email        varchar(100) not null,
    phone_number varchar(20)
);

create table patient_general_practice
(
    patient          integer references patients (nhs_number) on update cascade on delete cascade,
    general_practice integer references general_practices (id) on update cascade on delete cascade,
    from_date        varchar(100) not null,
    constraint primary key (patient, general_practice, from_date)
);

create table prescription_pickups
(
    prescription int references patients_prescriptions (id),
    staff        varchar(50) references staff_members (email),
    delivered_on timestamp
);