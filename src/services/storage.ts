import type { Member, OrganizationSettings } from '@/types/member';
const MEMBERS_KEY='data-sp-members';const SETTINGS_KEY='data-sp-settings';
export const defaultSettings:OrganizationSettings={namaOrganisasi:'DATA SP',logo:'',alamat:'Alamat organisasi serikat pekerja',whatsapp:'',email:'',darkMode:false};
export const loadData=():Member[]=>JSON.parse(localStorage.getItem(MEMBERS_KEY) || '[]');
export const saveData=(members:Member[])=>localStorage.setItem(MEMBERS_KEY,JSON.stringify(members));
export const deleteData=(id:string)=>{const next=loadData().filter(m=>m.id!==id);saveData(next);return next};
export const updateData=(member:Member)=>{const next=loadData().map(m=>m.id===member.id?member:m);saveData(next);return next};
export const loadSettings=():OrganizationSettings=>({...defaultSettings,...JSON.parse(localStorage.getItem(SETTINGS_KEY)||'{}')});
export const saveSettings=(settings:OrganizationSettings)=>localStorage.setItem(SETTINGS_KEY,JSON.stringify(settings));
