export const sections = ['Building','Mixing','Calender','Bead','Curing','Final Inspection','Warehouse','Utility','Engineering','Quality','Office','Security','HR','Finance','IT','Produksi','Lainnya'] as const;
export type Section = typeof sections[number];
export type SpStatus = 'Aktif'|'Hampir Habis'|'Expired';
export interface Member { id:string; nama:string; noCode:string; seksi:Section; masaBerlaku:string; keterangan:string; createdAt:string; updatedAt:string; }
export interface OrganizationSettings { namaOrganisasi:string; logo:string; alamat:string; whatsapp:string; email:string; darkMode:boolean; }
