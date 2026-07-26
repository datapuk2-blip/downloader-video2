import dayjs from 'dayjs';import type { SpStatus } from '@/types/member';
export const getSpStatus=(date:string):SpStatus=>{const today=dayjs().startOf('day');const exp=dayjs(date).startOf('day');const days=exp.diff(today,'day');if(days<0)return 'Expired';if(days<=30)return 'Hampir Habis';return 'Aktif'};
export const daysUntilExpiry=(date:string)=>dayjs(date).startOf('day').diff(dayjs().startOf('day'),'day');
export const isNotificationDay=(date:string)=>[30,15,7,1].includes(daysUntilExpiry(date));
export const statusClass=(s:SpStatus)=>s==='Aktif'?'bg-green-100 text-green-700 dark:bg-green-900/40 dark:text-green-200':s==='Hampir Habis'?'bg-amber-100 text-amber-700 dark:bg-amber-900/40 dark:text-amber-200':'bg-red-100 text-red-700 dark:bg-red-900/40 dark:text-red-200';
